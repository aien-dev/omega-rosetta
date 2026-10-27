#!/bin/sh
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# exercise.sh: test one Exercism-style exercise. Omega has no imports (units compose by
# concatenation), so the solution file and the exercise's test.om are joined into one unit,
# compiled with omc, and run. The test program prints one "ok N - ..." or "not ok N - ..." line
# per case and returns the number of failed cases.
#
#   sh exercise.sh exercises/leap                 test your exercises/leap/leap.om
#   sh exercise.sh exercises/leap path/to/sol.om  test another solution (CI uses .meta/example.om)
#
# The omc used is $OMC, else build/omega-mv/seed/out/omc left by run.sh; its sha256 must match
# omega.ref. stdout: the test lines, then "EXERCISE PASS <name>" or "EXERCISE FAIL <name> ...".
# Exit 0 when every case passes, 1 when a case fails or the solution does not compile or traps,
# 2 when setup fails.
set -u
here=$(cd "$(dirname "$0")" && pwd)
[ $# -ge 1 ] || { echo "usage: sh exercise.sh exercises/<name> [solution.om]" >&2; exit 2; }
dir=${1%/}
name=$(basename "$dir")
sol=${2:-$dir/$name.om}
omc=${OMC:-$here/build/omega-mv/seed/out/omc}
pin=$(awk '$1=="omc_sha256"{print $2}' "$here/omega.ref")
[ -f "$omc" ] || { echo "exercise.sh: no omc at $omc (run sh run.sh first, or set OMC)" >&2; exit 2; }
[ "$(sha256sum "$omc" | awk '{print $1}')" = "$pin" ] || { echo "exercise.sh: omc sha256 is not the pin in omega.ref" >&2; exit 2; }
[ -f "$sol" ] && [ -f "$dir/test.om" ] || { echo "exercise.sh: missing $sol or $dir/test.om" >&2; exit 2; }
tmp=$(mktemp -d) || exit 2
trap 'rm -rf "$tmp"' EXIT
cat "$sol" "$dir/test.om" > "$tmp/unit.om"
"$omc" < "$tmp/unit.om" > "$tmp/prog" 2> "$tmp/err"; crc=$?
if [ "$crc" != 0 ] || [ -s "$tmp/err" ]; then
    cat "$tmp/err" >&2
    echo "EXERCISE FAIL $name compile rc=$crc"
    exit 1
fi
chmod +x "$tmp/prog"
timeout 60 "$tmp/prog"; rc=$?
if [ "$rc" = 0 ]; then echo "EXERCISE PASS $name"; exit 0; fi
if [ "$rc" -gt 100 ]; then echo "EXERCISE FAIL $name trap $((rc - 100)) (exit $rc)"; else echo "EXERCISE FAIL $name failed=$rc"; fi
exit 1
