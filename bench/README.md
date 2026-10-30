# MultiPL-E for Omega

`bench/` adapts [MultiPL-E](https://github.com/nuprl/MultiPL-E) (pinned at
`3025a531af7450e7df8b96fe0440e9804480bbad`) to Omega's OM-2 profile. It turns the
HumanEval and MBPP problems into Omega prompts plus test programs and grades
completions with the pinned `omc` (`omega.ref`).

Status: IMPLEMENTED, and EXERCISED on a Linux AArch64 host (the DGX Spark's Grace
cores) with the stub model below. No language model has been evaluated yet, so no
model pass@k exists.

## Not first-party Omega

All Python here (`multipl-e/*.py`, `stub_model.py`, `score.py`) is a
**foreign-harness adapter**. MultiPL-E loads translators as Python classes
(`dataset_builder/humaneval_to_<ext>.py`) and evaluators as Python modules
(`evaluation/src/eval_<ext>.py`), so its plugin API can only be met in Python.
None of this code is first-party Omega. It sits outside every Omega product
path: nothing in omc, the seed or any shipped `.om` program depends on it. The
programs it writes are plain OM-2 compiled by the unmodified pinned omc.
`DEPENDENCIES.md` lists what it needs.

## Layout

| path | what |
|---|---|
| `multipl-e/humaneval_to_om.py` | The MultiPL-E `Translator` for Omega (`.om`). |
| `multipl-e/eval_om.py` | The MultiPL-E evaluator. `eval_script(path)` returns the MultiPL-E result dict. |
| `multipl-e/build_prompts.py` | Runs the translator through the pinned MultiPL-E `generic_translator`. It writes `prompts/`. |
| `prompts/{humaneval,mbpp}-om.jsonl` | The translated problems (name, language, prompt, tests, stop_tokens, …). |
| `prompts/*.coverage.json`, `prompts/COVERAGE.md` | Each problem's translation result, with a reason for every refusal. |
| `solutions/HumanEval_<n>.om` | Ten hand-written completions: function bodies up to and including `end`. |
| `stub_model.py` | Writes MultiPL-E completion files without a model. |
| `score.py` | Evaluates completion files and writes `<name>.results.json` and `summary.json` (pass@k). |
| `check.sh` | The gates. |
| `results/<mode>/` | The completions, results and summary from the last `check.sh` run. |
| `upstream/` | A prepared contribution to nuprl/MultiPL-E. It is **not submitted**. |

## Translation

Each problem becomes:

```
om2
note <docstring, MultiPL-E "reworded" terminology, doctests in Omega call syntax>
note <interface notes: renamed names, the result-array convention>
fn NAME PARAM TYPE ... to TYPE
<completion: the body and its closing end>
<tests>
```

| Python | Omega |
|---|---|
| `int` | `long` |
| `float` | `f64` |
| `bool` | `bool` |
| `List[int]` / `List[float]` | `view long *` / `view f64 *` |
| `str` | `view uchar *` (bytes; a non-ASCII test string is refused) |
| `Tuple[int, int]`, `Tuple[float, float]` (homogeneous) | `view long *` / `view f64 *` |
| list, string or tuple **result** | an extra last parameter `res edit T *`; the function returns the element count as `long` |

The tests become one `fn tc_K to bool` per assertion, then `fn main`.

- `main` returns `K+1` for the first failing case K. A translation holds at most
  98 cases, so this is 1..98.
- When every case holds, `main` writes the line `MultiPL-E Omega: all tests passed`
  and returns 0. The evaluator requires exit 0 **and** that final line. A completion
  that ends the process early with status 0 is therefore not a pass.
- A trap exits `100 + code`.
- Floats compare with exact `eq`, as MultiPL-E's Python tests compare with `==`.

### Refusals

The translator refuses a problem when OM-2 or the harness can't express it
faithfully. MultiPL-E then skips that problem.

- **Types:** `List[str]`, `List[bool]` (omc has no bool arrays), nested or compound
  lists, mixed tuples, `Optional`, `Union`, `Dict`, `Set`, `Any`, and unannotated or
  `None` results.
- **Values:** a non-ASCII string, an int outside i64, or a non-finite float.
- **ABI:** more than 6 argument slots.
- **Tests:** more than 98 cases, or a test that calls something other than the
  candidate.

### Renaming

The translator renames a name and adds a `note Omega name: X is Y here.` line
when the name:

- is a keyword;
- collides with a harness name;
- is a parameter longer than omc's 8-character local limit;
- is a function name longer than 8 characters whose first 8 bytes spell an
  8-letter keyword, such as `truncate_number`. Function names in this case get
  their first letter capitalised.

## Coverage (MEASURED, `prompts/COVERAGE.md`)

- **HumanEval: 129 of 164 translate.** MultiPL-E's originals already drop 3 of the
  164 (HumanEval_32, _38 and _50). Of its 161, the translator refuses 32:
  `List[str]` 17, compound list 4, `Optional` 3, `Union` 3, mixed tuple 3, `Dict` 2.
- **MBPP (`mbpp-typed`): 272 of 400 translate; 128 are refused.** The largest
  reasons are compound list 67, `List[str]` 22, mixed tuple 11 and `Dict` 10.

## Running

```sh
# prompts (needs a MultiPL-E clone at the pin; plain python3, no extra modules)
python3 bench/multipl-e/build_prompts.py --multipl-e ../MultiPL-E

# completions -> results -> pass@1
python3 bench/stub_model.py hand /tmp/run
OMEGA_OMC=/path/to/omc python3 bench/score.py /tmp/run

# all gates
sh bench/check.sh --omc /path/to/omc [--multipl-e ../MultiPL-E]
```

`eval_om.py` reads these settings from the environment:

- `OMEGA_OMC`: the omc path (required).
- `OMEGA_OMC_SHA256`: the pin. It defaults to `omega.ref`'s; on a mismatch the
  evaluator raises and records nothing.
- `OMEGA_EVAL_TIMEOUT`: seconds per program (default 15).
- `OMEGA_EVAL_WRAP`: an optional command prefix, for example
  `nice -n 19 taskset -c 10-14`.

omc writes static AArch64 Linux executables, so evaluation needs an AArch64 Linux
host. An x86-64 host would need qemu-user, which is NOT_RUN.

Outcome mapping:

| outcome | `om_status` | MultiPL-E `status` |
|---|---|---|
| omc exits nonzero or writes to stderr; the output is never run | `compile_error` | `SyntaxError` |
| exit 0 and the final pass line | `pass` | `OK` |
| exit 1..98 | `wrong_answer`, `om_case` = exit − 1 | `Exception` |
| exit 100..199 | `trap`, `om_case` = trap code | `Exception` |
| exit 0 without the pass line | `no_pass_line` | `Exception` |
| any other exit or a signal | `exit_other` | `Exception` |
| over the time limit (the process group is killed) | `timeout` | `Timeout` |

## Gates (`check.sh`)

Each gate has a negative control that must be observed failing:

| gate | passes when | negative control |
|---|---|---|
| `constants` | eval_om's pin equals `omega.ref`, and both files use the same pass line | a mismatch fails it |
| `prompts-rebuild` | rebuilding the prompts reproduces the committed files | a translator change fails it |
| `stub-sweep-{humaneval,mbpp}` | every translated problem compiles with the stub body `trap 14` and exits 114 in its first case | a broken test harness fails to compile or exits otherwise |
| `mode-hand` | the 10 hand solutions all reach `pass` | a deliberately broken solution is classified `wrong_answer` |
| `mode-wrong` | constant answers are all `wrong_answer` | — |
| `mode-invalid` | non-Omega text is always `compile_error` | — |
| `mode-trap` | `trap 5` is classified `trap` with case 5 | — |
| `mode-timeout` | a loop of about 2^72 steps is a `timeout` at 2 s | — |
| `pin-refusal` | eval_om refuses to evaluate when the omc hash is not the pin | — |
| `no-pass-line` | exit 0 without the pass line is not a pass | — |

The `wrong`, `invalid`, `trap` and `timeout` modes are themselves the negative
controls for `mode-hand`. A grader that passed everything would fail them.

The 10 hand solutions are HumanEval 0, 2, 3, 9, 13, 16, 27, 30, 48 and 53. They
cover these signatures:

- `List[float]` → `bool`
- `float` → `float`
- `List[int]` → `bool`
- `List[int]` → `List[int]` (twice)
- `int` → `int`
- `str` → `int`
- `str` → `str`
- `str` → `bool`

In the last run, pass@1 was 1.0 for `hand` and 0.0 for every other mode
(`results/*/summary.json`). With one completion per problem, pass@1 is c/n. The
values were checked with Wolfram (see the PR text in `upstream/`).

## omc defects worked around (pin e5b32567)

- **Keyword-prefix function names.** omc looks a function name up in the keyword
  table by its first 8 bytes. A longer name that starts with an 8-letter keyword,
  such as `truncate_number`, is refused with error 16 (`omc.om` `fn kw` caller near
  line 6681). The translator renames such names.
- **Empty text passed to a view.** An empty `text ""` passed to an unsized `view`
  parameter gives the callee a stale register as its length. `omc.om` arrarg takes
  `nm_len 0` to mean an unsized parameter. The result was a garbage `len`, and a
  segfault when the callee indexed the view. The translator passes `""` as
  `part a 0 0` instead.

Both are reported to the omega-mv omc owner. The pin is unchanged.
