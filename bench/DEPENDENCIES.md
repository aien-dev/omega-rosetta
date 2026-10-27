# bench/ dependencies

`bench/` is a foreign-harness adapter. MultiPL-E's plugin API is Python classes and
modules, so the adapter is Python. It is not first-party Omega and is outside every
Omega product path: omc, the seed and shipped `.om` programs use none of it.

| dependency | version | what it does here | Omega replacement |
|---|---|---|---|
| CPython | 3.12.3 (standard library only) | Runs the translator, evaluator, stub model, scorer and prompt builder. | None planned. MultiPL-E loads `humaneval_to_<ext>.py` and `eval_<ext>.py` as Python, so the adapter must be Python. The graded programs are plain OM-2. |
| MultiPL-E | `3025a531af7450e7df8b96fe0440e9804480bbad` (BSD 3-Clause with a Machine Learning Restriction) | `generic_translator.py`, `base_language_translator.py`, `terms.csv` and the HumanEval/MBPP originals. `build_prompts.py` copies them into `bench/build/` at run time; no MultiPL-E file is committed here. | None. It is the benchmark being adapted to. |
| omc | omega-mv `e5b32567a7aff3ce594e3254a622a846a6cd190b`, sha256 `2c82480596bbdc50cda9626866209ef662d5834f278f839ff4ce0250c495029f` (`omega.ref`) | Compiles every graded program. | First-party Omega already; used unmodified. |
| POSIX sh, awk, sha256sum, git | host versions | `check.sh`: pin check and the prompts-rebuild diff. | Verification tooling only. |
| Linux AArch64 | kernel with the AArch64 Linux ABI | Runs omc's static executables. | None needed. An x86-64 host would need qemu-user; that path is NOT_RUN. |

The adapter does not use numpy, `datasets` or `tqdm`. pass@k reimplements
MultiPL-E's `pass_k.estimator` in plain Python.

MultiPL-E's own `prepare_prompts_for_hfhub.py` imports `datasets`, so the
`upstream/` notes record a separate check with it in a throwaway venv. That is a
verification step only; nothing in `bench/` imports it.
