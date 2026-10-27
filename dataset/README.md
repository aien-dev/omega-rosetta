---
license: apache-2.0
language:
- en
- code
pretty_name: omega-rosetta
size_categories:
- n<1K
task_categories:
- text-generation
tags:
- code
- omega
- omegese
- rosetta-code
- exercism
configs:
- config_name: default
  data_files: omega-rosetta.parquet
---

# omega-rosetta

263 programs written in Omegese (the OM-2 profile of the Omega language) and compiled by `omc`, the
compiler that [aien-dev/omega-mv](https://github.com/aien-dev/omega-mv) rebuilds from a 408-byte
hand-written seed: 216 [Rosetta Code](https://rosettacode.org) tasks and 47 Exercism-style exercises.
Each task's expected output was written by an independent Python 3 oracle, never by `omc`.

The file is built from the repository by `python3 dataset/export.py` (needs `pyarrow`). It is not
published; this card describes the local build.

## Fields

One row per program, tasks first, each kind sorted by name.

| Column | Type | Meaning |
| --- | --- | --- |
| `name` | string | directory name, `tasks/<name>` or `exercises/<name>` |
| `kind` | string | `task` or `exercise` |
| `rosetta_url` | string | the Rosetta Code task page (tasks; null for exercises) |
| `exercism_url` | string | the Exercism problem page (exercises; null for tasks) |
| `title` | string | the Rosetta Code page title (tasks) or the exercise slug |
| `source_om` | string | the program: `tasks/<name>/<name>.om`, or for an exercise its reference solution `.meta/example.om` |
| `stub_om` | string | the exercise stub that traps (exit 113) until solved; null for tasks |
| `test_om` | string | the exercise's test cases, appended to a solution to form one unit; null for tasks |
| `expected_stdout` | string | `tasks/<name>/expected.txt` byte for byte; null for exercises, whose test unit prints `ok N - ...` lines |
| `expected_exit` | int32 | 0 for every row: a task exits 0, and `source_om` + `test_om` exits 0 when every case passes |
| `oracle_py` | string | the Python 3 standard-library program that wrote `expected_stdout`; null for exercises |
| `omc_sha256` | string | sha256 of the `omc` binary every row was checked with |
| `omega_mv_commit` | string | the aien-dev/omega-mv commit that births that `omc` |
| `lines` | int32 | lines of `source_om` that are not `note` comments |

## Provenance

- Repository: [aien-dev/omega-rosetta](https://github.com/aien-dev/omega-rosetta), branch `corpus/200`.
- Compiler pin ([`omega.ref`](../omega.ref)): omega-mv `e5b32567a7aff3ce594e3254a622a846a6cd190b`,
  `omc` sha256 `2c82480596bbdc50cda9626866209ef662d5834f278f839ff4ce0250c495029f`.
- Gate, Linux AArch64 (DGX Spark, Cortex-A725 cores 10-14), 2026-10-27, prebuilt pinned `omc`:
  `sh run.sh --omc <omc>` printed `TASKS PASS 216/216`; all 216 oracles reproduced their
  `expected.txt`; all 47 exercise examples passed through `exercise.sh` and all 47 stubs failed with
  trap 13. Negative controls failed as required: a mutated FizzBuzz answer (215/216), a one-bit
  change to the CRC-32 polynomial (215/216), a wrong leap solution (`failed=3`), and every
  `expected.txt` mutated at once (0/216, and 216/216 oracle comparisons caught it).
- Test cases of 42 exercises come from
  [exercism/problem-specifications](https://github.com/exercism/problem-specifications)
  `canonical-data.json` at commit `650bebeb39ad40439175288042aece982b0a90a9` (MIT; see
  [NOTICE](../NOTICE)). 49 number-theory tasks carry a `wolfram.txt` recording an independent
  Wolfram Language check of their expected output; that file is not a column here.

## Known limits

- One compiler at one commit. These programs say nothing about other `omc` versions, and passing
  them is not a proof that `omc` is correct.
- AArch64 Linux only: `omc` and the programs it writes are static AArch64 Linux ELF files.
- Every task's input is fixed in its source; Omega has no imports, so each program repeats its own
  output helpers, which inflates `lines` and makes rows look alike.
- Rosetta Code's `anagrams` and `ordered-words` tasks read `unixdict.txt`; these programs embed a small fixed sample instead,
  so their output differs from the full-list answers on rosettacode.org.
- Exercises carry no expected stdout; their check is the exit code of solution + tests.
- 3 non-ASCII cases of `reverse-string` were skipped; Omegese strings here are bytes.
- Rosetta Code publishes content under the GNU FDL 1.3; this dataset is the repository's own code
  under Apache-2.0 WITH LLVM-exception. It copies no Rosetta Code page prose; sample inputs that a
  task statement names (word lists, test strings) are reused as data.
