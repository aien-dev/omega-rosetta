#!/bin/sh
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# run.sh: compile every tasks/<name>/<name>.om with the pinned omc, run it, and compare its stdout
# byte for byte with tasks/<name>/expected.txt (written by an independent oracle, never by omc).
#
#   sh run.sh                  birth omc from the 408-byte seed at the omega-mv commit in omega.ref
#   sh run.sh --prebuilt       use omega-mv's committed seed/out/omc at that commit instead
#   sh run.sh --omc PATH       use an omc you already have (its sha256 must still match omega.ref)
#   sh run.sh --tasks DIR      check another task tree (the CI negative control uses this)
#
# stdout: one "PASS <task>" or "FAIL <task> <reason>" line per task, then "TASKS PASS <n>/<total>".
# stderr: diagnostics. Exit 0 when every task passes, 1 when any fails, 2 when setup fails.
# Linux AArch64 only: omc writes static AArch64 Linux ELF files (x86_64 hosts need qemu-user).
set -u
here=$(cd "$(dirname "$0")" && pwd)
tasks="$here/tasks"
omc=""
mode=seed
work="${WORK:-$here/build}"
while [ $# -gt 0 ]; do
    case "$1" in
        --prebuilt) mode=prebuilt ;;
        --omc) omc="$2"; mode=given; shift ;;
        --tasks) tasks="$2"; shift ;;
        --work) work="$2"; shift ;;
        *) echo "run.sh: unknown argument $1" >&2; exit 2 ;;
    esac
    shift
done
die() { echo "run.sh: $*" >&2; exit 2; }
ref=$(awk '$1=="commit"{print $2}' "$here/omega.ref")
pin=$(awk '$1=="omc_sha256"{print $2}' "$here/omega.ref")
[ -n "$ref" ] && [ -n "$pin" ] || die "omega.ref needs commit and omc_sha256 lines"
mkdir -p "$work" || die "cannot create $work"

if [ "$mode" != given ]; then
    src="$work/omega-mv"
    if [ ! -d "$src/.git" ]; then
        git clone -q --no-checkout https://github.com/aien-dev/omega-mv "$src" >&2 || die "clone failed"
    fi
    git -C "$src" checkout -q --detach "$ref" >&2 || die "omega-mv commit $ref not found"
    if [ "$mode" = seed ]; then
        echo "run.sh: birthing omc from seed at omega-mv $ref" >&2
        (cd "$src" && sh seed/omega-from-seed.sh) > "$work/seed.log" 2>&1 \
            || { tail -n 20 "$work/seed.log" >&2; die "seed/omega-from-seed.sh failed"; }
    fi
    omc="$src/seed/out/omc"
fi
[ -f "$omc" ] || die "no omc at $omc"
got=$(sha256sum "$omc" | awk '{print $1}')
[ "$got" = "$pin" ] || die "omc sha256 $got does not match the pin $pin"
echo "run.sh: omc sha256 $got (pin ok, mode $mode)" >&2

n=0; ok=0
for d in "$tasks"/*/; do
    name=$(basename "$d")
    [ -f "$d/$name.om" ] || continue
    n=$((n + 1))
    out="$work/out/$name"; mkdir -p "$out"
    "$omc" < "$d/$name.om" > "$out/prog" 2> "$out/compile.err"; crc=$?
    if [ "$crc" != 0 ] || [ -s "$out/compile.err" ]; then
        echo "FAIL $name compile rc=$crc $(head -c 200 "$out/compile.err" | tr '\n' ' ')"
        continue
    fi
    chmod +x "$out/prog"
    timeout 120 "$out/prog" > "$out/stdout" 2> "$out/stderr"; rrc=$?
    if [ "$rrc" != 0 ]; then echo "FAIL $name run rc=$rrc"; continue; fi
    if ! cmp -s "$out/stdout" "$d/expected.txt"; then
        echo "FAIL $name stdout differs from expected.txt"
        diff "$d/expected.txt" "$out/stdout" | head -n 10 >&2
        continue
    fi
    ok=$((ok + 1)); echo "PASS $name"
done
[ "$n" -gt 0 ] || die "no tasks under $tasks"
echo "TASKS PASS $ok/$n"
[ "$ok" = "$n" ]
