# Upstream package for nuprl/MultiPL-E (PUBLISH-QUEUE, not submitted)

This is not sent. Submitting it posts outside aien-dev and needs Drake's OK for
this one item.

- Target: `nuprl/MultiPL-E`, branch `main`, based on
  `3025a531af7450e7df8b96fe0440e9804480bbad`.
- Patch: `0001-Add-Omega-OM-2-translator-and-evaluator.patch`. Apply it with
  `git am` or `git apply`. It adds 610 lines in 5 files and deletes none.
- `dataset_builder/terms.csv` uses CRLF line endings. The patch keeps them, and
  `bench/.gitattributes` stops git from rewriting the patch file.

How it was checked (2026-10-27, Linux AArch64):

1. `git apply --check` succeeded on a fresh clone at the base commit, and the patch
   then applied.
2. MultiPL-E's own `dataset_builder/prepare_prompts_for_hfhub.py` ran in the patched
   tree with `--lang humaneval_to_om.py --doctests transform --prompt-terminology
   reworded`. HumanEval gave 129 problems and `mbpp-typed` gave 272. Their `prompt`,
   `tests`, `stop_tokens` and `language` fields equal `bench/prompts/*.jsonl` for
   every problem. The script imports `datasets`, so this check ran in a throwaway
   venv with `datasets` 5.1.0.
3. In the patched `evaluation/src`, `containerized_eval.eval_string_script("om", …)`
   ran on the two completions in `evaluation/test_inputs/om-hand-0.0-keep-HumanEval53.json`
   with `OMEGA_OMC` set. The results were `OK` (exit 0) and `SyntaxError` (omc error 4),
   which is the "first OK, second fails" shape the other `test_inputs` use.

NOT_RUN:

- The MultiPL-E evaluation container. Its Dockerfile is `ubuntu:22.04` with amd64-only
  apt sources, and omc writes AArch64 executables.
- Any model.
- `evaluation/src/main.py --testing`, because the host has no `tqdm`.

---

## PR title

Add Omega (OM-2) as a MultiPL-E language

## PR body

This adds [Omega](https://github.com/aien-dev/omega-mv) as a MultiPL-E target
language with file extension `.om`. Omega is a small systems language with its
own compiler, `omc`, which writes static AArch64 Linux executables directly.

**What is added**

- `dataset_builder/humaneval_to_om.py` is the `Translator`. Each problem becomes an
  OM-2 `fn` signature preceded by `note` lines that carry the docstring. Doctests
  are transformed into Omega call syntax.
  - Type mapping: `int`→`long`, `float`→`f64`, `bool`→`bool`,
    `List[int]`/`List[float]`→`view long *`/`view f64 *`, `str`→`view uchar *`,
    and homogeneous numeric tuples→views.
  - A list, string or tuple result becomes a trailing `res edit T *` parameter, and
    the function returns the element count.
  - The tests become one Omega function per assertion plus a `main`. `main` exits
    with `K+1` when case K fails. When every case holds, it prints
    `MultiPL-E Omega: all tests passed` and exits 0.
  - The translator refuses (returns `None`, with a reason) every type or value it
    can't express faithfully: `List[str]`, nested lists, mixed tuples,
    `Optional`, `Union`, `Dict`, `Set`, `Any`, non-ASCII strings, ints outside
    i64, and calls with more than 6 argument slots.
  - Coverage at this base commit: HumanEval 129 of the 161 originals (161 of the
    164 problems), MBPP (`mbpp-typed`) 272 of 400.
- `evaluation/src/eval_om.py` compiles with `omc` and runs the program. It uses
  only the standard library.
  - Compile failure, or any omc diagnostic, is `SyntaxError`.
  - A pass is `OK` and requires exit 0 **and** the final pass line.
  - A wrong answer or a trap is `Exception`, and a time-out is `Timeout`.
  - Each run gets its own process group, which is killed on time-out.
- `terms.csv` gets the row `Omega,om,array,array,array,dictionary,none,true,false`.
  Omega has no dictionary or None value, and problems that use them are refused.
- `containerized_eval.py` gets the `"om"` entry.
- `evaluation/test_inputs/om-hand-0.0-keep-HumanEval53.json` holds one passing and
  one non-compiling completion.

**Running it**

Set `OMEGA_OMC` to an `omc` binary. `eval_om.py` checks its sha256 against
`OMEGA_OMC_SHA256`, which defaults to the pinned build: omega-mv
`e5b32567a7aff3ce594e3254a622a846a6cd190b`, sha256
`2c82480596bbdc50cda9626866209ef662d5834f278f839ff4ce0250c495029f`. If the hash
doesn't match, it refuses to evaluate, so results always name one compiler.
`OMEGA_EVAL_TIMEOUT` sets the per-program limit in seconds (default 15).

omc targets Linux AArch64 only. The current evaluation image is amd64, so this PR
does **not** change the Dockerfile. Two options, neither tried:

- Build the image for `linux/arm64`.
- Add `qemu-user` to the amd64 image and set `OMEGA_EVAL_WRAP=qemu-aarch64`.
  omc is itself an AArch64 executable, and the prefix applies to both omc and the
  compiled program.

An arm64 image could fetch the pinned compiler as follows:

```dockerfile
RUN git clone https://github.com/aien-dev/omega-mv /omega && \
    git -C /omega checkout e5b32567a7aff3ce594e3254a622a846a6cd190b
ENV OMEGA_OMC=/omega/seed/out/omc
```

`seed/omega-from-seed.sh` in that repository can instead rebuild omc from its
408-byte seed.

**Evidence**

The adapter's own gate suite is `bench/check.sh` in
[aien-dev/omega-rosetta](https://github.com/aien-dev/omega-rosetta). It compiles
every translated HumanEval and MBPP problem with a stub body.

| completions | pass@1 |
|---|---|
| 10 hand-written HumanEval solutions | 1.0 |
| constant wrong answers | 0.0 (all `wrong_answer`) |
| invalid syntax | 0.0 (all `SyntaxError`) |
| traps | 0.0 (all `trap`) |
| infinite loops | 0.0 (all `Timeout`) |

No language model was evaluated for this PR.

**Licence**

The contribution is offered under MultiPL-E's licence (BSD 3-Clause with the
Machine Learning Restriction in `LICENSE`).

---

## Wolfram check of the pass@k values

The `bench/score.py` estimator matches MultiPL-E's `pass_k.estimator`. Its pass@k
values were checked with Wolfram:

```
WolframLanguageEvaluator:
  est[n_,c_,k_] := If[n - c < k, 1, 1 - Binomial[n - c, k]/Binomial[n, k]];
  {Mean[Table[est[1,1,1],10]], Mean[Table[est[1,0,1],10]],
   N[est[20,7,1],17], N[est[20,7,10],17], N[est[200,13,100],17], N[est[5,3,10],17]}
-> {1, 0, 0.35, 0.99845201238390093, 0.99991949719880544, 1.}
```

`score.estimator` gave `0.3500000000000001`, `0.9984520123839009`,
`0.9999194971988055` and `1.0` for the last four. They agree to double precision.
