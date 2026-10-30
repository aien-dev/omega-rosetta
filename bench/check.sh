#!/bin/sh
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# bench/check.sh: gates for the MultiPL-E Omega adapter (bench/README.md).
#
#   sh bench/check.sh --omc PATH [--multipl-e DIR]
#
# PATH must hash to omc_sha256 in omega.ref. With --multipl-e (a MultiPL-E clone at
# MULTIPLE_E_PIN in bench/multipl-e/build_prompts.py) the prompts are rebuilt and must equal the
# committed ones; without it that gate prints NOT_RUN. Writes bench/results/<mode>/ (committed)
# and bench/build/.
# stdout: "PASS <gate>", "FAIL <gate> ..." or "NOT_RUN <gate> ..." lines, then "BENCH PASS|FAIL".
# Exit 0 when no gate fails, 1 when one fails, 2 when setup fails. Linux AArch64 only.
set -u
bench=$(cd "$(dirname "$0")" && pwd)
root=$(dirname "$bench")
omc="${OMEGA_OMC:-}"
mpe=""
while [ $# -gt 0 ]; do
    case "$1" in
        --omc) omc="$2"; shift ;;
        --multipl-e) mpe="$2"; shift ;;
        *) echo "check.sh: unknown argument $1" >&2; exit 2 ;;
    esac
    shift
done
die() { echo "check.sh: $*" >&2; exit 2; }
pin=$(awk '$1=="omc_sha256"{print $2}' "$root/omega.ref")
[ -n "$pin" ] || die "omega.ref has no omc_sha256 line"
[ -n "$omc" ] && [ -f "$omc" ] || die "give --omc PATH (or OMEGA_OMC)"
got=$(sha256sum "$omc" | awk '{print $1}')
[ "$got" = "$pin" ] || die "omc sha256 $got does not match the pin $pin"
OMEGA_OMC=$omc; OMEGA_OMC_SHA256=$pin; export OMEGA_OMC OMEGA_OMC_SHA256
work="$bench/build/check"; rm -rf "$work"; mkdir -p "$work" || die "cannot create $work"
fails=0
pass() { echo "PASS $1"; }
fail() { echo "FAIL $*"; fails=$((fails + 1)); }

# 1. The pin and the pass line are written in two files; they must agree.
if python3 - "$bench" "$pin" <<'EOF'
import sys
sys.path.insert(0, sys.argv[1] + "/multipl-e")
import eval_om, humaneval_to_om
ok = eval_om.PINNED_OMC_SHA256 == sys.argv[2] and eval_om.MPE_OK_LINE == humaneval_to_om.MPE_OK_LINE
sys.exit(0 if ok else 1)
EOF
then pass constants; else fail constants "eval_om pin or pass line differs"; fi

# 2. The committed prompts are what the translator writes.
if [ -n "$mpe" ]; then
    if python3 -W ignore "$bench/multipl-e/build_prompts.py" --multipl-e "$mpe" > "$work/build.log" 2>&1 \
        && git -C "$root" diff --quiet -- bench/prompts; then
        pass prompts-rebuild
    else
        fail prompts-rebuild "see $work/build.log and git diff bench/prompts"
    fi
else
    echo "NOT_RUN prompts-rebuild (no --multipl-e)"
fi

# 3. Every translated prompt and its tests compile: the stub body traps 14 in the first case.
for set in humaneval mbpp; do
    python3 "$bench/stub_model.py" stub "$work/stub-$set" --prompts "$bench/prompts/$set-om.jsonl" >&2 \
        && python3 "$bench/score.py" --expect trap:14 "$work/stub-$set" > "$work/stub-$set.log" \
        && pass "stub-sweep-$set $(head -n 1 "$work/stub-$set.log")" \
        || fail "stub-sweep-$set" "$(grep FAIL "$work/stub-$set.log" | head -n 3)"
done

# 4. Hand solutions pass; each negative control is classified as what it is.
for spec in hand:pass wrong:wrong_answer invalid:compile_error trap:trap:5 timeout:timeout; do
    mode=${spec%%:*}; want=${spec#*:}
    out="$bench/results/$mode"; rm -rf "$out"
    python3 "$bench/stub_model.py" "$mode" "$out" >&2 || { fail "mode-$mode" "stub_model failed"; continue; }
    t=15; [ "$mode" = timeout ] && t=2
    if OMEGA_EVAL_TIMEOUT=$t python3 "$bench/score.py" --expect "$want" "$out" > "$work/$mode.log"; then
        pass "mode-$mode $want $(cat "$work/$mode.log" | head -n 1)"
    else
        fail "mode-$mode" "$(cat "$work/$mode.log")"
    fi
done

# 5. eval_om refuses an omc that is not the pin (negative control: a wrong pin).
printf 'om2\nfn main to int\nret 0\nend\n' > "$work/bare.om"
if OMEGA_OMC_SHA256=0000000000000000000000000000000000000000000000000000000000000000 \
    python3 "$bench/multipl-e/eval_om.py" "$work/bare.om" > "$work/pin.log" 2>&1; then
    fail pin-refusal "eval_om ran with a wrong pin"
elif grep -q "refusing to evaluate" "$work/pin.log"; then
    pass pin-refusal
else
    fail pin-refusal "$(tail -n 1 "$work/pin.log")"
fi

# 6. Exit 0 alone is not a pass: a program that never writes the pass line.
if python3 "$bench/multipl-e/eval_om.py" "$work/bare.om" | grep -q '"om_status": "no_pass_line"'; then
    pass no-pass-line
else
    fail no-pass-line "exit 0 without the pass line was not no_pass_line"
fi

if [ "$fails" -eq 0 ]; then echo "BENCH PASS"; exit 0; fi
echo "BENCH FAIL ($fails)"; exit 1
