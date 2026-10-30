# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
"""Export the omega-rosetta corpus as one Parquet file for a Hugging Face dataset.

    python3 dataset/export.py [--out dataset/omega-rosetta.parquet]

Needs pyarrow (use a virtual environment). Reads only files in this repository; it does not run
omc or any oracle. Run `sh run.sh` first: the dataset card records that gate's result, and this
script refuses a task whose expected.txt is missing.

One row per task (tasks/<name>) and per exercise (exercises/<name>), sorted by kind then name.
"""
import argparse
import hashlib
import os
import re
import sys

import pyarrow as pa
import pyarrow.parquet as pq

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SCHEMA = pa.schema([
    ("name", pa.string()),
    ("kind", pa.string()),
    ("rosetta_url", pa.string()),
    ("exercism_url", pa.string()),
    ("title", pa.string()),
    ("source_om", pa.string()),
    ("stub_om", pa.string()),
    ("test_om", pa.string()),
    ("expected_stdout", pa.string()),
    ("expected_exit", pa.int32()),
    ("oracle_py", pa.string()),
    ("omc_sha256", pa.string()),
    ("omega_mv_commit", pa.string()),
    ("lines", pa.int32()),
])

HEADER = re.compile(r'^note Rosetta Code task "(.+)": (https://rosettacode\.org/wiki/\S+)$')


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def pin():
    ref = {}
    for line in read(os.path.join(ROOT, "omega.ref")).splitlines():
        parts = line.split()
        if len(parts) == 2 and not line.startswith("#"):
            ref[parts[0]] = parts[1]
    return ref["commit"], ref["omc_sha256"]


def code_lines(src):
    """Lines that are not note comments, as the README table counts them."""
    return sum(1 for l in src.splitlines() if not (l.startswith("note ") or l == "note"))


def exercism_url(readme, name):
    m = re.search(r"\| \[`%s`\]\([^)]*\) \| \[[^\]]*\]\((https://exercism\.org/[^)]+)\) \|" % re.escape(name), readme)
    if not m:
        sys.exit("export.py: no README row with an exercism.org link for exercise " + name)
    return m.group(1)


def rows():
    commit, sha = pin()
    readme = read(os.path.join(ROOT, "README.md"))
    out = []
    tasks = os.path.join(ROOT, "tasks")
    for name in sorted(os.listdir(tasks)):
        d = os.path.join(tasks, name)
        src = read(os.path.join(d, name + ".om"))
        m = HEADER.match(src.splitlines()[0])
        if not m:
            sys.exit("export.py: %s.om does not start with the Rosetta Code task note" % name)
        out.append({
            "name": name, "kind": "task", "rosetta_url": m.group(2), "exercism_url": None,
            "title": m.group(1), "source_om": src, "stub_om": None, "test_om": None,
            "expected_stdout": read(os.path.join(d, "expected.txt")), "expected_exit": 0,
            "oracle_py": read(os.path.join(d, "oracle.py")), "omc_sha256": sha,
            "omega_mv_commit": commit, "lines": code_lines(src),
        })
    exercises = os.path.join(ROOT, "exercises")
    for name in sorted(os.listdir(exercises)):
        d = os.path.join(exercises, name)
        src = read(os.path.join(d, ".meta", "example.om"))
        out.append({
            "name": name, "kind": "exercise", "rosetta_url": None,
            "exercism_url": exercism_url(readme, name), "title": name, "source_om": src,
            "stub_om": read(os.path.join(d, name + ".om")), "test_om": read(os.path.join(d, "test.om")),
            "expected_stdout": None, "expected_exit": 0, "oracle_py": None, "omc_sha256": sha,
            "omega_mv_commit": commit, "lines": code_lines(src),
        })
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=os.path.join(HERE, "omega-rosetta.parquet"))
    args = ap.parse_args()
    data = rows()
    table = pa.Table.from_pylist(data, schema=SCHEMA)
    pq.write_table(table, args.out, compression="zstd")
    h = hashlib.sha256()
    with open(args.out, "rb") as f:
        h.update(f.read())
    kinds = {k: sum(1 for r in data if r["kind"] == k) for k in ("task", "exercise")}
    print("%s rows=%d tasks=%d exercises=%d sha256=%s" % (args.out, len(data), kinds["task"], kinds["exercise"], h.hexdigest()))


if __name__ == "__main__":
    main()
