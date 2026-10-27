# omega-rosetta

24 classic [Rosetta Code](https://rosettacode.org) tasks and 5 Exercism-style exercises, written in
Omega's source language, Omegese, and compiled by `omc`, the compiler that
[aien-dev/omega-mv](https://github.com/aien-dev/omega-mv) rebuilds from a 408-byte hand-written seed.
I wrote this so you can read real Omega next to the languages you already know, run every program
yourself, and see each answer checked against a reference that Omega had no hand in.

About that seed, plainly: `omc` is rebuilt from a 408-byte hand-written AArch64 Linux program (seed0)
through four seed rungs to a 325,524-byte compiler, with no C compiler, assembler or linker writing
any byte of the chain. The 408 bytes are a binary written as 7,903 bytes of commented hex text and turned into bytes by a 1,048-byte POSIX shell script (load0.sh); the shell's printf is the one outside tool, and the chain runs only on AArch64 Linux. Rebuilding gives the committed binary byte for byte. This is a fixed-output reproducibility match along one build path from a pinned commit; it is not diverse double compilation and does not prove omc correct.

```sh
git clone https://github.com/aien-dev/omega-rosetta && cd omega-rosetta && sh run.sh
```

`run.sh` clones omega-mv at the commit pinned in [`omega.ref`](omega.ref), births `omc` from the seed
with `seed/omega-from-seed.sh`, checks that the compiler's sha256 is the pinned
`2c82480596bbdc50cda9626866209ef662d5834f278f839ff4ce0250c495029f`, then compiles and runs every task
and compares its output byte for byte with `tasks/<name>/expected.txt`. It prints one `PASS` or
`FAIL` line per task and `TASKS PASS <passed>/<total>`, and exits 0 only when every task passes.
`sh run.sh --prebuilt` uses omega-mv's committed `seed/out/omc` (same sha256 check) instead of the
seed birth; `sh run.sh --omc PATH` uses a compiler you already have.

**You need Linux on AArch64** (a Raspberry Pi 4/5 on a 64-bit OS, an Arm cloud VM, Apple silicon
running Linux, a GitHub `ubuntu-24.04-arm` runner), POSIX `sh`, `git`, `sha256sum` and `timeout`.
`omc` is a static AArch64 Linux program and writes static AArch64 Linux programs. On x86_64 it only
runs under an emulator such as qemu-user (`qemu-aarch64`); I have not run this repository that way.

## Where it stands

| Check | Level | Where |
| --- | --- | --- |
| Tasks pass on a GitHub `ubuntu-24.04-arm` runner, compiler born from the seed | EXERCISED | [tasks workflow](.github/workflows/ci.yml) |
| Negative controls (mutated answer, mutated source, unsolved stubs, wrong solution) fail | EXERCISED | same workflow |
| Every `expected.txt` is reproduced by its `oracle.py` | EXERCISED | same workflow |
| Code posted to rosettacode.org | PROPOSED | [`drafts/rosettacode/`](drafts/rosettacode/) |

This is a host CPU check of compiled programs on Linux AArch64. It says nothing about speed, and
it is not a claim that `omc` is correct beyond these programs.

## Tasks

Each task directory holds the program (`<name>.om`), its expected output (`expected.txt`) and the
oracle that wrote it (`oracle.py`, Python 3 standard library only). `omc` never wrote an
`expected.txt`. Line counts leave out `note` comment lines; every file repeats its small output
helpers because Omega has no imports (see the notes below).

| Program | Rosetta Code task | Lines | Oracle uses |
| --- | --- | ---: | --- |
| [`99-bottles-of-beer`](tasks/99-bottles-of-beer/99-bottles-of-beer.om) | [99 bottles of beer](https://rosettacode.org/wiki/99_bottles_of_beer) | 60 | plain Python |
| [`ackermann-function`](tasks/ackermann-function/ackermann-function.om) | [Ackermann function](https://rosettacode.org/wiki/Ackermann_function) | 52 | `sys` |
| [`binary-digits`](tasks/binary-digits/binary-digits.om) | [Binary digits](https://rosettacode.org/wiki/Binary_digits) | 35 | plain Python |
| [`binary-search`](tasks/binary-search/binary-search.om) | [Binary search](https://rosettacode.org/wiki/Binary_search) | 92 | `bisect` |
| [`bubble-sort`](tasks/bubble-sort/bubble-sort.om) | [Sorting algorithms/Bubble sort](https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort) | 78 | plain Python |
| [`crc-32`](tasks/crc-32/crc-32.om) | [CRC-32](https://rosettacode.org/wiki/CRC-32) | 46 | `zlib` |
| [`factorial`](tasks/factorial/factorial.om) | [Factorial](https://rosettacode.org/wiki/Factorial) | 42 | `math` |
| [`fibonacci-sequence`](tasks/fibonacci-sequence/fibonacci-sequence.om) | [Fibonacci sequence](https://rosettacode.org/wiki/Fibonacci_sequence) | 43 | plain Python |
| [`fizzbuzz`](tasks/fizzbuzz/fizzbuzz.om) | [FizzBuzz](https://rosettacode.org/wiki/FizzBuzz) | 49 | plain Python |
| [`greatest-common-divisor`](tasks/greatest-common-divisor/greatest-common-divisor.om) | [Greatest common divisor](https://rosettacode.org/wiki/Greatest_common_divisor) | 57 | `math` |
| [`hailstone-sequence`](tasks/hailstone-sequence/hailstone-sequence.om) | [Hailstone sequence](https://rosettacode.org/wiki/Hailstone_sequence) | 81 | plain Python |
| [`hello-world`](tasks/hello-world/hello-world.om) | [Hello world/Text](https://rosettacode.org/wiki/Hello_world/Text) | 16 | plain Python |
| [`insertion-sort`](tasks/insertion-sort/insertion-sort.om) | [Sorting algorithms/Insertion sort](https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort) | 76 | plain Python |
| [`leap-year`](tasks/leap-year/leap-year.om) | [Leap year](https://rosettacode.org/wiki/Leap_year) | 54 | `calendar` |
| [`mandelbrot-set`](tasks/mandelbrot-set/mandelbrot-set.om) | [Mandelbrot set](https://rosettacode.org/wiki/Mandelbrot_set) | 46 | plain Python |
| [`n-queens-problem`](tasks/n-queens-problem/n-queens-problem.om) | [N-queens problem](https://rosettacode.org/wiki/N-queens_problem) | 65 | `itertools` |
| [`perfect-numbers`](tasks/perfect-numbers/perfect-numbers.om) | [Perfect numbers](https://rosettacode.org/wiki/Perfect_numbers) | 52 | plain Python |
| [`prime-decomposition`](tasks/prime-decomposition/prime-decomposition.om) | [Prime decomposition](https://rosettacode.org/wiki/Prime_decomposition) | 64 | plain Python |
| [`reverse-a-string`](tasks/reverse-a-string/reverse-a-string.om) | [Reverse a string](https://rosettacode.org/wiki/Reverse_a_string) | 28 | plain Python |
| [`roman-numerals-encode`](tasks/roman-numerals-encode/roman-numerals-encode.om) | [Roman numerals/Encode](https://rosettacode.org/wiki/Roman_numerals/Encode) | 70 | plain Python |
| [`rot-13`](tasks/rot-13/rot-13.om) | [Rot-13](https://rosettacode.org/wiki/Rot-13) | 35 | `codecs` |
| [`sha-256`](tasks/sha-256/sha-256.om) | [SHA-256](https://rosettacode.org/wiki/SHA-256) | 208 | `hashlib` |
| [`sieve-of-eratosthenes`](tasks/sieve-of-eratosthenes/sieve-of-eratosthenes.om) | [Sieve of Eratosthenes](https://rosettacode.org/wiki/Sieve_of_Eratosthenes) | 48 | plain Python |
| [`towers-of-hanoi`](tasks/towers-of-hanoi/towers-of-hanoi.om) | [Towers of Hanoi](https://rosettacode.org/wiki/Towers_of_Hanoi) | 47 | plain Python |

The SHA-256 round constants and initial values in `tasks/sha-256/sha-256.om` were copied
mechanically from omega-mv's [`om/sha256/sha256-om2.om`](https://github.com/aien-dev/omega-mv/blob/e5b32567a7aff3ce594e3254a622a846a6cd190b/om/sha256/sha256-om2.om); the hashes
are checked against Python's `hashlib`, and "Rosetta code" gives Rosetta Code's published value
`764faf5c…cdfcf`.

## Exercises

Five small problems in the Exercism style. Each `exercises/<name>/<name>.om` is a stub that traps
until you write the function; `test.om` holds the cases.

```sh
sh run.sh                              # once, to birth omc into build/
sh exercise.sh exercises/leap          # test your exercises/leap/leap.om
```

Omega has no imports, so `exercise.sh` joins your file and `test.om` into one unit, compiles it and
runs it. You get one `ok N - ...` or `not ok N - ...` line per case and `EXERCISE PASS <name>` when
all pass. Reference solutions are in `exercises/<name>/.meta/example.om`.

| Stub | Problem |
| --- | --- |
| [`armstrong-numbers`](exercises/armstrong-numbers/armstrong-numbers.om) | [armstrong-numbers](https://exercism.org/tracks/python/exercises/armstrong-numbers) |
| [`collatz-conjecture`](exercises/collatz-conjecture/collatz-conjecture.om) | [collatz-conjecture](https://exercism.org/tracks/python/exercises/collatz-conjecture) |
| [`difference-of-squares`](exercises/difference-of-squares/difference-of-squares.om) | [difference-of-squares](https://exercism.org/tracks/python/exercises/difference-of-squares) |
| [`grains`](exercises/grains/grains.om) | [grains](https://exercism.org/tracks/python/exercises/grains) |
| [`leap`](exercises/leap/leap.om) | [leap](https://exercism.org/tracks/python/exercises/leap) |

## Reading Omega in ten minutes

These are the things I would want to know before opening the first file. The full guide is
[OM-2 tutorial](https://github.com/aien-dev/omega-mv/blob/e5b32567a7aff3ce594e3254a622a846a6cd190b/docs/one_layer/OM2-TUTORIAL.md), the language reference is
[OMEGESE.md](https://github.com/aien-dev/omega-mv/blob/e5b32567a7aff3ce594e3254a622a846a6cd190b/docs/one_layer/OMEGESE.md), and [om2-tour.om](https://github.com/aien-dev/omega-mv/blob/e5b32567a7aff3ce594e3254a622a846a6cd190b/examples/om2-tour.om) is a
single runnable tour.

- **Prefix words, one statement per line.** `add a mul b c` is `a + b * c`. Every operator is a
  word with a fixed number of operands, so there are no parentheses and no precedence.
- **The first line that is not a `note` picks the profile.** Every file here starts with `om2`, which
  allows unsized views (`view uchar *`) and slices (`part a start count`).
- **Types are explicit and never mix silently.** `uchar ushort uint ulong`, `char short int long`,
  `f32 f64`, `bool`. A literal takes the type its context needs; when there is none, name it:
  `c = uint 0xffffffff`. Converting is a word: `ulong k`, `bitcast ulong n`.
- **Assignment declares.** `x = ulong 0` makes a local; later `x = add x 1` updates it. A name first
  set inside a block ends with that block.
- **Arrays and access.** `d = new uchar 20 0` makes a local array; `get a i` reads, `put a i v` writes.
  An index out of range traps (exit 103), never a wild write. `global seq ulong 1000` is a zeroed global array.
- **Functions and parameters.** `fn gcd a ulong b ulong to ulong` … `end`. Array parameters say how
  they are used: `view` (read only) or `edit` (may write).
- **Every loop has a bound.** `while cond bound 999` and `for i ulong 10`. A loop that runs past its
  bound traps (exit 104), so no loop here can spin forever.
- **Traps and exit codes.** `trap 13` stops the program with exit code 113 (100 + code). Compiler
  errors print `omc: line N: error K` and exit with K.
- **Names are short.** Locals, globals and texts have at most 8 characters, function names up to 63.
  Operator and host words are reserved (`neg` is negation, so the minus-sign text is `minus`).
- **No imports, no standard library.** A program is one unit; units compose by concatenation. Output
  is the host word `write 1 buf offset count`, which is why each task carries `emit`/`emitu` helpers.

## Benchmark

- [`bench/`](bench/): a MultiPL-E adapter for Omega. It translates HumanEval (129/164) and MBPP (272/400) into OM-2 prompts and tests, and grades completions with the pinned `omc`. It includes 10 hand solutions and the gates (`sh bench/check.sh --omc PATH`). See [bench/README.md](bench/README.md).

## Rosetta Code drafts

[`drafts/rosettacode/`](drafts/rosettacode/) holds one ready-to-paste `.wiki` section per task and
the steps to add the language. Rosetta Code's `Category:Omega` already describes two unrelated
languages called Omega (Günther Blaschek's prototype-based language and Tim Sheard's functional
language), so the drafts use the language's own name, **Omegese**, under a new `Category:Omegese`,
plus a one-line pointer on `Category:Omega`. Nothing has been posted; see
[`drafts/rosettacode/STEPS.txt`](drafts/rosettacode/STEPS.txt).

## Foreign dependencies

None of these is part of an Omega program; they fetch, check or drive. Every task binary is written
by `omc` alone.

| Tool | Version | Purpose | Omega replacement |
| --- | --- | --- | --- |
| POSIX `sh`, `awk`, `cmp`, `diff`, `cat`, `mktemp`, `timeout` | runner image (Ubuntu 24.04 coreutils/dash) | `run.sh`, `exercise.sh` driver glue | an Omega driver once omega-mv grows process spawning words for tests; the host words `fork`/`execprog`/`waitpid` exist today |
| `sha256sum` | GNU coreutils | pin check of `omc` | omega-mv's own SHA-256 in `om/sha256` |
| `git` | runner image | clone omega-mv at the pin | none planned; a verification tool |
| Python 3 standard library | 3.12 on the runner | independent oracles that write `expected.txt` | none: an oracle must stay independent of Omega |
| GitHub Actions `actions/checkout@v4`, `actions/upload-artifact@v4` | v4 | CI | none planned |

## Connected repos

- [aien-dev/omega-mv](https://github.com/aien-dev/omega-mv) at [`e5b32567`](https://github.com/aien-dev/omega-mv/tree/e5b32567a7aff3ce594e3254a622a846a6cd190b): the parent; the seed, `omc` and the language docs. Pinned in [`omega.ref`](omega.ref).
- [aien-dev/omega-seed-challenge](https://github.com/aien-dev/omega-seed-challenge): rebuild `omc` from the 408-byte seed yourself and check every rung.
- [aien-dev/omega-kernel-template](https://github.com/aien-dev/omega-kernel-template): one Omega kernel turned into SPIR-V and checked against AArch64.

## Contributing

New tasks are welcome. Add `tasks/<name>/<name>.om`, an `oracle.py` that does not use Omega, and the
`expected.txt` it prints; `sh run.sh` must pass. Sign off your commits (`git commit -s`).

## Licence

Apache-2.0 WITH LLVM-exception ([LICENSE](LICENSE), [NOTICE](NOTICE)). Code posted to Rosetta Code
is also published there under the GNU Free Documentation License 1.3, the site's content licence.
