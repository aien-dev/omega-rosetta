#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
"""Stub "model" for the Omega MultiPL-E harness: writes MultiPL-E completion files
without calling any model server.

    stub_model.py MODE OUTDIR [--prompts bench/prompts/humaneval-om.jsonl]

One ``<name>.json`` per problem, in the layout ``multipl_e.completions`` writes
(name, language, temperature, top_p, max_tokens, prompt, tests, completions,
stop_tokens), one completion each. Mode ``stub`` covers every problem in the
prompts file; the other modes cover the problems with a hand solution in
bench/solutions/.

MODE    completion                                     expected om_status
hand    bench/solutions/HumanEval_<n>.om               pass
wrong   a constant of the return type (0 / 0.0 / false) wrong_answer
invalid text that is not Omega                         compile_error
trap    trap 5                                         trap, case 5
timeout three nested loops of 2^24 (about 2^72 steps)  timeout
stub    trap 14 (the translator's prompt stub)         trap, case 14

Foreign-harness tooling, not first-party Omega; outside every product path.
"""

import json
import re
import sys
from pathlib import Path

BENCH = Path(__file__).resolve().parent
MODES = ("hand", "wrong", "invalid", "trap", "timeout", "stub")
_RET = re.compile(r"^fn \S+ (?:.* )?to (\w+)$", re.M)


def ret_type(prompt: str) -> str:
    return list(_RET.finditer(prompt))[-1].group(1)


def default(t: str) -> str:
    return {"bool": "false", "f64": "0.0"}.get(t, "0")


def completion(mode: str, problem: dict, hand: str) -> str:
    t = ret_type(problem["prompt"])
    if mode == "hand":
        return hand
    if mode == "wrong":
        return f"ret {default(t)}\nend\n"
    if mode == "invalid":
        return "this is ( not Omega\nend\n"
    if mode == "trap":
        return "trap 5\nend\n"
    if mode == "timeout":
        return (
            "n = ulong 0\n"
            "for i ulong 16777216\nfor j ulong 16777216\nfor k ulong 16777216\n"
            "n = xor n k\nend\nend\nend\n"
            f"ret {default(t)}\nend\n"
        )
    if mode == "stub":
        return "trap 14\nend\n"
    raise ValueError(mode)


def main(argv):
    if len(argv) < 2 or argv[0] not in MODES:
        print(__doc__, file=sys.stderr)
        return 2
    mode, out = argv[0], Path(argv[1])
    prompts = Path(argv[3]) if len(argv) > 3 and argv[2] == "--prompts" else BENCH / "prompts/humaneval-om.jsonl"
    problems = [json.loads(line) for line in prompts.read_text().splitlines()]
    if mode == "stub":
        work = [(p, "") for p in problems]
    else:
        by_number = {p["name"].split("_")[1]: p for p in problems}
        sols = sorted((BENCH / "solutions").glob("HumanEval_*.om"), key=lambda s: int(s.stem.split("_")[1]))
        work = []
        for sol in sols:
            p = by_number.get(sol.stem.split("_")[1])
            if p is None:
                print(f"stub_model: {sol.name} has no translated prompt", file=sys.stderr)
                return 1
            work.append((p, sol.read_text()))
    if not work:
        print("stub_model: nothing to write", file=sys.stderr)
        return 1
    out.mkdir(parents=True, exist_ok=True)
    for p, hand in work:
        record = {
            "name": p["name"],
            "language": p["language"],
            "temperature": 0.0,
            "top_p": 1.0,
            "max_tokens": 0,
            "prompt": p["prompt"],
            "tests": p["tests"],
            "completions": [completion(mode, p, hand)],
            "stop_tokens": p["stop_tokens"],
            "stub_mode": mode,
        }
        (out / f"{p['name']}.json").write_text(json.dumps(record, indent=2) + "\n")
    print(f"stub_model: {mode}: {len(work)} problems -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
