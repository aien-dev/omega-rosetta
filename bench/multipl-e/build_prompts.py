#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
"""Translate MultiPL-E's Python benchmarks to Omega and report coverage.

Foreign-harness adapter (see bench/DEPENDENCIES.md). It runs MultiPL-E's own
dataset_builder/generic_translator.py, at the pinned MultiPL-E commit, with
humaneval_to_om.Translator, exactly as prepare_prompts_for_hfhub.py would, but
without the Hugging Face `datasets` dependency, and it records WHY each refused
problem was refused.

    bench/multipl-e/build_prompts.py --multipl-e /path/to/MultiPL-E [--out bench/prompts]

Writes, per benchmark: <bench>-om.jsonl (MultiPL-E prompt records) and
<bench>-om.coverage.json, plus COVERAGE.md summarising both.
"""

import argparse
import collections
import contextlib
import importlib
import io
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BENCH = HERE.parent
MULTIPLE_E_PIN = "3025a531af7450e7df8b96fe0440e9804480bbad"
# The upstream HumanEval has 164 problems; MultiPL-E's originals keep 161 (it drops
# HumanEval_32, _38 and _50, whose tests call helpers outside the prompt).
UPSTREAM_SIZES = {"humaneval": 164, "mbpp": None}
# (benchmark, originals directory, doctests mode, prompt terminology): the
# configurations MultiPL-E publishes as humaneval-<lang> and mbpp-<lang>.
CONFIGS = [
    ("humaneval", "originals-with-cleaned-doctests", "transform", "reworded"),
    ("mbpp", "mbpp-typed", "transform", "reworded"),
]
# Columns: name, ext, list, array, tuple, dictionary, None, True, False. Omega has no
# dictionary or None value; problems that use them are refused, so those words never land.
TERMS_ROW = "Omega,om,array,array,array,dictionary,none,true,false\n"


def pinned_multiple_e(root: Path) -> None:
    head = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True, check=True
    ).stdout.strip()
    if head != MULTIPLE_E_PIN:
        sys.exit(f"build_prompts: MultiPL-E at {head}, pin is {MULTIPLE_E_PIN}; refusing")


def workdir(root: Path) -> Path:
    """A scratch dataset_builder: MultiPL-E's translator modules plus ours, and
    terms.csv with the Omega row (generic_translator reads ./terms.csv on import)."""
    wd = BENCH / "build" / "dataset_builder"
    if wd.exists():
        shutil.rmtree(wd)
    wd.mkdir(parents=True)
    for f in ("generic_translator.py", "base_language_translator.py", "terms.csv"):
        shutil.copy(root / "dataset_builder" / f, wd / f)
    shutil.copy(HERE / "humaneval_to_om.py", wd / "humaneval_to_om.py")
    terms = (wd / "terms.csv").read_text()
    if "\nOmega,om," not in terms:
        (wd / "terms.csv").write_text(terms.rstrip("\n") + "\n" + TERMS_ROW)
    return wd


def reason_from_log(log: str) -> str:
    if "Failed to translate tests" in log:
        return "tests:not all asserts are `assert f(...) == v` (MultiPL-E generic translator)"
    if "Conflicting tests" in log:
        return "tests:conflicting duplicate asserts"
    if "Exception translating prompt" in log:
        return "prompt:docstring or doctest not parseable (MultiPL-E generic translator)"
    if "Exception translating test case" in log:
        return "tests:expression outside MultiPL-E's literal grammar"
    if "No tests were translated" in log:
        return "tests:none"
    return "unknown"


def build(root: Path, out: Path) -> dict:
    pinned_multiple_e(root)
    wd = workdir(root)
    cwd = os.getcwd()
    os.chdir(wd)
    sys.path.insert(0, str(wd))
    try:
        gt = importlib.import_module("generic_translator")
        om = importlib.import_module("humaneval_to_om")
        summary = {}
        for bench, originals, doctests, terminology in CONFIGS:
            translator = om.Translator()
            files = sorted(
                (root / "datasets" / originals).glob("*.py"),
                key=lambda p: int(p.name.split("_")[1]),
            )
            records, rows = [], []
            for f in files:
                name = f.name[: -len(".py")]
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                    result = gt.translate_prompt_and_tests(f, translator, doctests, terminology)
                if result is None:
                    r = translator.refusal
                    code = r.code if r is not None else reason_from_log(buf.getvalue())
                    detail = r.detail if r is not None else ""
                    rows.append({"name": name, "translated": False, "reason": code, "detail": detail})
                    continue
                prompt, tests = result
                records.append(
                    {
                        "name": name,
                        "language": translator.file_ext(),
                        "prompt": prompt,
                        "doctests": doctests,
                        "original": f"datasets/{originals}/{f.name}",
                        "prompt_terminology": terminology,
                        "tests": tests,
                        "stop_tokens": gt.get_stop_from_translator(translator),
                    }
                )
                rows.append({"name": name, "translated": True, "cases": len(translator.cases)})
            with open(out / f"{bench}-om.jsonl", "w") as fh:
                for rec in records:
                    fh.write(json.dumps(rec) + "\n")
            reasons = collections.Counter(r["reason"] for r in rows if not r["translated"])
            cov = {
                "benchmark": bench,
                "originals": f"datasets/{originals}",
                "multipl_e_commit": MULTIPLE_E_PIN,
                "omega_mv_pin": om.OMEGA_MV_PIN,
                "doctests": doctests,
                "prompt_terminology": terminology,
                "upstream_size": UPSTREAM_SIZES[bench],
                "originals_count": len(files),
                "translated": len(records),
                "refused": len(files) - len(records),
                "reasons": dict(reasons.most_common()),
                "problems": rows,
            }
            with open(out / f"{bench}-om.coverage.json", "w") as fh:
                json.dump(cov, fh, indent=1)
                fh.write("\n")
            summary[bench] = cov
        return summary
    finally:
        os.chdir(cwd)
        sys.path.remove(str(wd))


def coverage_md(summary: dict) -> str:
    lines = [
        "# MultiPL-E Omega coverage",
        "",
        "Generated by `bench/multipl-e/build_prompts.py`; do not edit by hand.",
        f"MultiPL-E `{MULTIPLE_E_PIN}`, omega-mv pin `{next(iter(summary.values()))['omega_mv_pin']}`.",
        "",
    ]
    for bench, cov in summary.items():
        up = cov["upstream_size"]
        lines.append(f"## {bench}")
        lines.append("")
        if up:
            lines.append(
                f"{cov['translated']} of {up} translate ({up - cov['originals_count']} are already "
                f"dropped by MultiPL-E's originals, {cov['refused']} of its {cov['originals_count']} are refused here)."
            )
        else:
            lines.append(f"{cov['translated']} of {cov['originals_count']} translate; {cov['refused']} refused.")
        lines += ["", "| refusal reason | problems |", "|---|---|"]
        for reason, n in cov["reasons"].items():
            lines.append(f"| `{reason}` | {n} |")
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--multipl-e", default=os.environ.get("MULTIPL_E"), help="MultiPL-E checkout at the pin")
    ap.add_argument("--out", default=str(BENCH / "prompts"))
    args = ap.parse_args()
    if not args.multipl_e:
        sys.exit("build_prompts: pass --multipl-e DIR or set MULTIPL_E")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    summary = build(Path(args.multipl_e).resolve(), out)
    (out / "COVERAGE.md").write_text(coverage_md(summary))
    for bench, cov in summary.items():
        print(f"{bench}: {cov['translated']}/{cov['upstream_size'] or cov['originals_count']} translated "
              f"({cov['originals_count']} originals, {cov['refused']} refused)")


if __name__ == "__main__":
    main()
