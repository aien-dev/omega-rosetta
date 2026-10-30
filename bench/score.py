#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
"""Evaluate MultiPL-E completion files with eval_om and summarise pass@k.

    OMEGA_OMC=/path/to/omc score.py [--expect OM_STATUS[:CASE]] DIR [DIR ...]

For every ``DIR/<name>.json`` this writes ``DIR/<name>.results.json`` in the
format of MultiPL-E ``evaluation/src/main.py`` (the completion record without
``completions``, plus ``results``: program, stdout, stderr, exit_code, status,
timestamp; eval_om also adds om_status / om_case), then prints one JSON summary
line per DIR and writes it to ``DIR/summary.json``. The program is
prompt + completion + "\\n" + tests, exactly as upstream builds it. pass@k is
upstream pass_k.py's unbiased estimator, counting status "OK" with exit_code 0.

Foreign-harness tooling, not first-party Omega; outside every product path.
"""

import collections
import json
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "multipl-e"))
import eval_om  # noqa: E402


def estimator(n: int, c: int, k: int) -> float:
    """1 - C(n-c, k) / C(n, k), computed as pass_k.py does, without numpy."""
    if n - c < k:
        return 1.0
    prod = 1.0
    for i in range(n - c + 1, n + 1):
        prod *= 1.0 - k / i
    return 1.0 - prod


def evaluate(problem: dict) -> list:
    results = []
    for completion in problem["completions"]:
        program = problem["prompt"] + completion + "\n" + problem["tests"]
        with tempfile.NamedTemporaryFile(suffix=".om") as f:
            f.write(program.encode("utf-8"))
            f.flush()
            r = eval_om.eval_script(Path(f.name))
        results.append({"program": program, **r, "timestamp": int(time.time())})
    return results


def score_dir(d: Path) -> dict:
    per_problem, kinds = [], collections.Counter()
    for path in sorted(d.glob("*.json")):
        if path.name.endswith(".results.json") or path.name == "summary.json":
            continue
        problem = json.loads(path.read_text())
        record = {k: v for k, v in problem.items() if k != "completions"}
        record["results"] = evaluate(problem)
        (d / (path.name[: -len(".json")] + ".results.json")).write_text(json.dumps(record, indent=2) + "\n")
        n = len(record["results"])
        c = sum(1 for r in record["results"] if r["status"] == "OK" and r["exit_code"] == 0)
        kinds.update(r["om_status"] for r in record["results"])
        per_problem.append({"name": problem["name"], "n": n, "c": c,
                            "om_status": [r["om_status"] for r in record["results"]]})
    if not per_problem:
        raise SystemExit(f"score: no completion files in {d}")
    summary = {
        "dir": d.name,
        "problems": len(per_problem),
        "pass@1": sum(estimator(p["n"], p["c"], 1) for p in per_problem) / len(per_problem),
        "om_status": dict(sorted(kinds.items())),
        "per_problem": per_problem,
    }
    (d / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary


def main(argv):
    expect = None
    if argv[:1] == ["--expect"] and len(argv) > 1:
        expect, argv = argv[1].split(":"), argv[2:]
    if not argv:
        print(__doc__, file=sys.stderr)
        return 2
    rc = 0
    for d in argv:
        s = score_dir(Path(d))
        print(json.dumps({k: v for k, v in s.items() if k != "per_problem"}))
        if expect is None:
            continue
        for p in s["per_problem"]:
            results = json.loads((Path(d) / (p["name"] + ".results.json")).read_text())["results"]
            for r in results:
                got = [r["om_status"]] + ([str(r["om_case"])] if len(expect) > 1 else [])
                if got != expect:
                    print(f"score: FAIL {p['name']}: expected {':'.join(expect)}, got {':'.join(got)}")
                    rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
