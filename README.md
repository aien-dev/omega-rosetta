# omega-rosetta

216 classic [Rosetta Code](https://rosettacode.org) tasks and 47 Exercism-style exercises, written in
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
| Negative controls (mutated answer, mutated source, unsolved stubs, wrong solution, every answer mutated at once) fail | EXERCISED | same workflow |
| Every `expected.txt` is reproduced by its `oracle.py` | EXERCISED | same workflow |
| Code posted to rosettacode.org | PROPOSED | [`drafts/rosettacode/`](drafts/rosettacode/) |
| Hugging Face dataset of the corpus | PROPOSED, built locally only | [`dataset/`](dataset/) |

This is a host CPU check of compiled programs on Linux AArch64. It says nothing about speed, and
it is not a claim that `omc` is correct beyond these programs.

## Tasks

Each task directory holds the program (`<name>.om`), its expected output (`expected.txt`) and the
oracle that wrote it (`oracle.py`, Python 3 standard library only). `omc` never wrote an
`expected.txt`. Line counts leave out `note` comment lines; every file repeats its small output
helpers because Omega has no imports (see the notes below).

| Program | Rosetta Code task | Lines | Oracle uses |
| --- | --- | ---: | --- |
| [`100-doors`](tasks/100-doors/100-doors.om) | [100 doors](https://rosettacode.org/wiki/100_doors) | 50 | plain Python |
| [`99-bottles-of-beer`](tasks/99-bottles-of-beer/99-bottles-of-beer.om) | [99 bottles of beer](https://rosettacode.org/wiki/99_bottles_of_beer) | 60 | plain Python |
| [`abc-problem`](tasks/abc-problem/abc-problem.om) | [ABC problem](https://rosettacode.org/wiki/ABC_problem) | 72 | plain Python |
| [`abelian-sandpile-model`](tasks/abelian-sandpile-model/abelian-sandpile-model.om) | [Abelian sandpile model](https://rosettacode.org/wiki/Abelian_sandpile_model) | 88 | plain Python |
| [`abundant-deficient-and-perfect-number-classifications`](tasks/abundant-deficient-and-perfect-number-classifications/abundant-deficient-and-perfect-number-classifications.om) | [Abundant, deficient and perfect number classifications](https://rosettacode.org/wiki/Abundant,_deficient_and_perfect_number_classifications) | 70 | `math` |
| [`ackermann-function`](tasks/ackermann-function/ackermann-function.om) | [Ackermann function](https://rosettacode.org/wiki/Ackermann_function) | 52 | `sys` |
| [`additive-primes`](tasks/additive-primes/additive-primes.om) | [Additive primes](https://rosettacode.org/wiki/Additive_primes) | 87 | plain Python |
| [`almost-prime`](tasks/almost-prime/almost-prime.om) | [Almost prime](https://rosettacode.org/wiki/Almost_prime) | 66 | plain Python |
| [`amicable-pairs`](tasks/amicable-pairs/amicable-pairs.om) | [Amicable pairs](https://rosettacode.org/wiki/Amicable_pairs) | 54 | `math` |
| [`anagrams`](tasks/anagrams/anagrams.om) | [Anagrams](https://rosettacode.org/wiki/Anagrams) | 112 | plain Python |
| [`anti-primes`](tasks/anti-primes/anti-primes.om) | [Anti-primes](https://rosettacode.org/wiki/Anti-primes) | 60 | plain Python |
| [`array-concatenation`](tasks/array-concatenation/array-concatenation.om) | [Array concatenation](https://rosettacode.org/wiki/Array_concatenation) | 56 | plain Python |
| [`attractive-numbers`](tasks/attractive-numbers/attractive-numbers.om) | [Attractive numbers](https://rosettacode.org/wiki/Attractive_numbers) | 78 | plain Python |
| [`bacon-cipher`](tasks/bacon-cipher/bacon-cipher.om) | [Bacon cipher](https://rosettacode.org/wiki/Bacon_cipher) | 78 | plain Python |
| [`base64-encode-data`](tasks/base64-encode-data/base64-encode-data.om) | [Base64 encode data](https://rosettacode.org/wiki/Base64_encode_data) | 55 | `base64` |
| [`bead-sort`](tasks/bead-sort/bead-sort.om) | [Sorting algorithms/Bead sort](https://rosettacode.org/wiki/Sorting_algorithms/Bead_sort) | 109 | plain Python |
| [`bell-numbers`](tasks/bell-numbers/bell-numbers.om) | [Bell numbers](https://rosettacode.org/wiki/Bell_numbers) | 104 | `math` |
| [`binary-digits`](tasks/binary-digits/binary-digits.om) | [Binary digits](https://rosettacode.org/wiki/Binary_digits) | 35 | plain Python |
| [`binary-search`](tasks/binary-search/binary-search.om) | [Binary search](https://rosettacode.org/wiki/Binary_search) | 92 | `bisect` |
| [`bogosort`](tasks/bogosort/bogosort.om) | [Sorting algorithms/Bogosort](https://rosettacode.org/wiki/Sorting_algorithms/Bogosort) | 119 | plain Python |
| [`bubble-sort`](tasks/bubble-sort/bubble-sort.om) | [Sorting algorithms/Bubble sort](https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort) | 78 | plain Python |
| [`caesar-cipher`](tasks/caesar-cipher/caesar-cipher.om) | [Caesar cipher](https://rosettacode.org/wiki/Caesar_cipher) | 38 | plain Python |
| [`camel-case-and-snake-case`](tasks/camel-case-and-snake-case/camel-case-and-snake-case.om) | [Camel case and snake case](https://rosettacode.org/wiki/Camel_case_and_snake_case) | 106 | plain Python |
| [`catalan-numbers`](tasks/catalan-numbers/catalan-numbers.om) | [Catalan numbers](https://rosettacode.org/wiki/Catalan_numbers) | 55 | `math` |
| [`character-codes`](tasks/character-codes/character-codes.om) | [Character codes](https://rosettacode.org/wiki/Character_codes) | 44 | plain Python |
| [`cocktail-sort`](tasks/cocktail-sort/cocktail-sort.om) | [Sorting algorithms/Cocktail sort](https://rosettacode.org/wiki/Sorting_algorithms/Cocktail_sort) | 114 | plain Python |
| [`cocktail-sort-with-shifting-bounds`](tasks/cocktail-sort-with-shifting-bounds/cocktail-sort-with-shifting-bounds.om) | [Sorting algorithms/Cocktail sort with shifting bounds](https://rosettacode.org/wiki/Sorting_algorithms/Cocktail_sort_with_shifting_bounds) | 114 | plain Python |
| [`comb-sort`](tasks/comb-sort/comb-sort.om) | [Sorting algorithms/Comb sort](https://rosettacode.org/wiki/Sorting_algorithms/Comb_sort) | 103 | plain Python |
| [`combinations`](tasks/combinations/combinations.om) | [Combinations](https://rosettacode.org/wiki/Combinations) | 70 | plain Python |
| [`combinations-with-repetitions`](tasks/combinations-with-repetitions/combinations-with-repetitions.om) | [Combinations with repetitions](https://rosettacode.org/wiki/Combinations_with_repetitions) | 82 | `itertools`, `math` |
| [`comma-quibbling`](tasks/comma-quibbling/comma-quibbling.om) | [Comma quibbling](https://rosettacode.org/wiki/Comma_quibbling) | 59 | plain Python |
| [`conways-game-of-life`](tasks/conways-game-of-life/conways-game-of-life.om) | [Conway's Game of Life](https://rosettacode.org/wiki/Conway's_Game_of_Life) | 118 | `collections` |
| [`copy-a-string`](tasks/copy-a-string/copy-a-string.om) | [Copy a string](https://rosettacode.org/wiki/Copy_a_string) | 33 | plain Python |
| [`count-how-many-vowels-and-consonants-occur-in-a-string`](tasks/count-how-many-vowels-and-consonants-occur-in-a-string/count-how-many-vowels-and-consonants-occur-in-a-string.om) | [Count how many vowels and consonants occur in a string](https://rosettacode.org/wiki/Count_how_many_vowels_and_consonants_occur_in_a_string) | 77 | plain Python |
| [`count-in-factors`](tasks/count-in-factors/count-in-factors.om) | [Count in factors](https://rosettacode.org/wiki/Count_in_factors) | 70 | plain Python |
| [`count-occurrences-of-a-substring`](tasks/count-occurrences-of-a-substring/count-occurrences-of-a-substring.om) | [Count occurrences of a substring](https://rosettacode.org/wiki/Count_occurrences_of_a_substring) | 56 | plain Python |
| [`count-the-coins`](tasks/count-the-coins/count-the-coins.om) | [Count the coins](https://rosettacode.org/wiki/Count_the_coins) | 64 | plain Python |
| [`counting-sort`](tasks/counting-sort/counting-sort.om) | [Sorting algorithms/Counting sort](https://rosettacode.org/wiki/Sorting_algorithms/Counting_sort) | 108 | plain Python |
| [`crc-32`](tasks/crc-32/crc-32.om) | [CRC-32](https://rosettacode.org/wiki/CRC-32) | 46 | `zlib` |
| [`cuban-primes`](tasks/cuban-primes/cuban-primes.om) | [Cuban primes](https://rosettacode.org/wiki/Cuban_primes) | 129 | plain Python |
| [`cycle-sort`](tasks/cycle-sort/cycle-sort.om) | [Sorting algorithms/Cycle sort](https://rosettacode.org/wiki/Sorting_algorithms/Cycle_sort) | 125 | plain Python |
| [`determinant-and-permanent`](tasks/determinant-and-permanent/determinant-and-permanent.om) | [Determinant and permanent](https://rosettacode.org/wiki/Determinant_and_permanent) | 194 | `fractions` |
| [`determine-if-a-string-has-all-the-same-characters`](tasks/determine-if-a-string-has-all-the-same-characters/determine-if-a-string-has-all-the-same-characters.om) | [Determine if a string has all the same characters](https://rosettacode.org/wiki/Determine_if_a_string_has_all_the_same_characters) | 71 | plain Python |
| [`determine-if-a-string-has-all-unique-characters`](tasks/determine-if-a-string-has-all-unique-characters/determine-if-a-string-has-all-unique-characters.om) | [Determine if a string has all unique characters](https://rosettacode.org/wiki/Determine_if_a_string_has_all_unique_characters) | 73 | plain Python |
| [`determine-if-a-string-is-collapsible`](tasks/determine-if-a-string-is-collapsible/determine-if-a-string-is-collapsible.om) | [Determine if a string is collapsible](https://rosettacode.org/wiki/Determine_if_a_string_is_collapsible) | 66 | `itertools` |
| [`determine-if-a-string-is-numeric`](tasks/determine-if-a-string-is-numeric/determine-if-a-string-is-numeric.om) | [Determine if a string is numeric](https://rosettacode.org/wiki/Determine_if_a_string_is_numeric) | 104 | plain Python |
| [`determine-if-a-string-is-squeezable`](tasks/determine-if-a-string-is-squeezable/determine-if-a-string-is-squeezable.om) | [Determine if a string is squeezable](https://rosettacode.org/wiki/Determine_if_a_string_is_squeezable) | 78 | `re` |
| [`digital-root`](tasks/digital-root/digital-root.om) | [Digital root](https://rosettacode.org/wiki/Digital_root) | 62 | plain Python |
| [`dijkstras-algorithm`](tasks/dijkstras-algorithm/dijkstras-algorithm.om) | [Dijkstra's algorithm](https://rosettacode.org/wiki/Dijkstra's_algorithm) | 133 | plain Python |
| [`dutch-national-flag-problem`](tasks/dutch-national-flag-problem/dutch-national-flag-problem.om) | [Dutch national flag problem](https://rosettacode.org/wiki/Dutch_national_flag_problem) | 121 | plain Python |
| [`elementary-cellular-automaton`](tasks/elementary-cellular-automaton/elementary-cellular-automaton.om) | [Elementary cellular automaton](https://rosettacode.org/wiki/Elementary_cellular_automaton) | 76 | plain Python |
| [`emirp-primes`](tasks/emirp-primes/emirp-primes.om) | [Emirp primes](https://rosettacode.org/wiki/Emirp_primes) | 102 | plain Python |
| [`empty-string`](tasks/empty-string/empty-string.om) | [Empty string](https://rosettacode.org/wiki/Empty_string) | 40 | plain Python |
| [`equilibrium-index`](tasks/equilibrium-index/equilibrium-index.om) | [Equilibrium index](https://rosettacode.org/wiki/Equilibrium_index) | 113 | plain Python |
| [`ethiopian-multiplication`](tasks/ethiopian-multiplication/ethiopian-multiplication.om) | [Ethiopian multiplication](https://rosettacode.org/wiki/Ethiopian_multiplication) | 69 | plain Python |
| [`evaluate-binomial-coefficients`](tasks/evaluate-binomial-coefficients/evaluate-binomial-coefficients.om) | [Evaluate binomial coefficients](https://rosettacode.org/wiki/Evaluate_binomial_coefficients) | 66 | `math` |
| [`extensible-prime-generator`](tasks/extensible-prime-generator/extensible-prime-generator.om) | [Extensible prime generator](https://rosettacode.org/wiki/Extensible_prime_generator) | 96 | `itertools` |
| [`factorial`](tasks/factorial/factorial.om) | [Factorial](https://rosettacode.org/wiki/Factorial) | 42 | `math` |
| [`factors-of-an-integer`](tasks/factors-of-an-integer/factors-of-an-integer.om) | [Factors of an integer](https://rosettacode.org/wiki/Factors_of_an_integer) | 66 | plain Python |
| [`fibonacci-n-step-number-sequences`](tasks/fibonacci-n-step-number-sequences/fibonacci-n-step-number-sequences.om) | [Fibonacci n-step number sequences](https://rosettacode.org/wiki/Fibonacci_n-step_number_sequences) | 82 | plain Python |
| [`fibonacci-sequence`](tasks/fibonacci-sequence/fibonacci-sequence.om) | [Fibonacci sequence](https://rosettacode.org/wiki/Fibonacci_sequence) | 43 | plain Python |
| [`fizzbuzz`](tasks/fizzbuzz/fizzbuzz.om) | [FizzBuzz](https://rosettacode.org/wiki/FizzBuzz) | 49 | plain Python |
| [`floyd-warshall-algorithm`](tasks/floyd-warshall-algorithm/floyd-warshall-algorithm.om) | [Floyd-Warshall algorithm](https://rosettacode.org/wiki/Floyd-Warshall_algorithm) | 125 | plain Python |
| [`floyds-triangle`](tasks/floyds-triangle/floyds-triangle.om) | [Floyd's triangle](https://rosettacode.org/wiki/Floyd's_triangle) | 74 | plain Python |
| [`fusc-sequence`](tasks/fusc-sequence/fusc-sequence.om) | [Fusc sequence](https://rosettacode.org/wiki/Fusc_sequence) | 73 | `functools` |
| [`generate-lower-case-ascii-alphabet`](tasks/generate-lower-case-ascii-alphabet/generate-lower-case-ascii-alphabet.om) | [Generate lower case ASCII alphabet](https://rosettacode.org/wiki/Generate_lower_case_ASCII_alphabet) | 21 | `string` |
| [`gnome-sort`](tasks/gnome-sort/gnome-sort.om) | [Sorting algorithms/Gnome sort](https://rosettacode.org/wiki/Sorting_algorithms/Gnome_sort) | 101 | plain Python |
| [`gray-code`](tasks/gray-code/gray-code.om) | [Gray code](https://rosettacode.org/wiki/Gray_code) | 86 | plain Python |
| [`greatest-common-divisor`](tasks/greatest-common-divisor/greatest-common-divisor.om) | [Greatest common divisor](https://rosettacode.org/wiki/Greatest_common_divisor) | 57 | `math` |
| [`greatest-subsequential-sum`](tasks/greatest-subsequential-sum/greatest-subsequential-sum.om) | [Greatest subsequential sum](https://rosettacode.org/wiki/Greatest_subsequential_sum) | 127 | plain Python |
| [`hailstone-sequence`](tasks/hailstone-sequence/hailstone-sequence.om) | [Hailstone sequence](https://rosettacode.org/wiki/Hailstone_sequence) | 81 | plain Python |
| [`hamming-numbers`](tasks/hamming-numbers/hamming-numbers.om) | [Hamming numbers](https://rosettacode.org/wiki/Hamming_numbers) | 78 | `heapq` |
| [`happy-numbers`](tasks/happy-numbers/happy-numbers.om) | [Happy numbers](https://rosettacode.org/wiki/Happy_numbers) | 62 | plain Python |
| [`harshad-or-niven-series`](tasks/harshad-or-niven-series/harshad-or-niven-series.om) | [Harshad or Niven series](https://rosettacode.org/wiki/Harshad_or_Niven_series) | 60 | `itertools` |
| [`heapsort`](tasks/heapsort/heapsort.om) | [Sorting algorithms/Heapsort](https://rosettacode.org/wiki/Sorting_algorithms/Heapsort) | 117 | plain Python |
| [`hello-world`](tasks/hello-world/hello-world.om) | [Hello world/Text](https://rosettacode.org/wiki/Hello_world/Text) | 16 | plain Python |
| [`hello-world-newline-omission`](tasks/hello-world-newline-omission/hello-world-newline-omission.om) | [Hello world/Newline omission](https://rosettacode.org/wiki/Hello_world/Newline_omission) | 16 | plain Python |
| [`hofstadter-figure-figure-sequences`](tasks/hofstadter-figure-figure-sequences/hofstadter-figure-figure-sequences.om) | [Hofstadter Figure-Figure sequences](https://rosettacode.org/wiki/Hofstadter_Figure-Figure_sequences) | 95 | `itertools` |
| [`hofstadter-q-sequence`](tasks/hofstadter-q-sequence/hofstadter-q-sequence.om) | [Hofstadter Q sequence](https://rosettacode.org/wiki/Hofstadter_Q_sequence) | 61 | plain Python |
| [`identity-matrix`](tasks/identity-matrix/identity-matrix.om) | [Identity matrix](https://rosettacode.org/wiki/Identity_matrix) | 51 | plain Python |
| [`insertion-sort`](tasks/insertion-sort/insertion-sort.om) | [Sorting algorithms/Insertion sort](https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort) | 76 | plain Python |
| [`isbn13-check-digit`](tasks/isbn13-check-digit/isbn13-check-digit.om) | [ISBN13 check digit](https://rosettacode.org/wiki/ISBN13_check_digit) | 49 | plain Python |
| [`isqrt-integer-square-root-of-x`](tasks/isqrt-integer-square-root-of-x/isqrt-integer-square-root-of-x.om) | [Isqrt (integer square root) of X](https://rosettacode.org/wiki/Isqrt_(integer_square_root)_of_X) | 68 | `math` |
| [`jewels-and-stones`](tasks/jewels-and-stones/jewels-and-stones.om) | [Jewels and stones](https://rosettacode.org/wiki/Jewels_and_stones) | 56 | plain Python |
| [`josephus-problem`](tasks/josephus-problem/josephus-problem.om) | [Josephus problem](https://rosettacode.org/wiki/Josephus_problem) | 61 | plain Python |
| [`kaprekar-numbers`](tasks/kaprekar-numbers/kaprekar-numbers.om) | [Kaprekar numbers](https://rosettacode.org/wiki/Kaprekar_numbers) | 65 | plain Python |
| [`knapsack-problem-0-1`](tasks/knapsack-problem-0-1/knapsack-problem-0-1.om) | [Knapsack problem/0-1](https://rosettacode.org/wiki/Knapsack_problem/0-1) | 131 | `itertools` |
| [`knapsack-problem-unbounded`](tasks/knapsack-problem-unbounded/knapsack-problem-unbounded.om) | [Knapsack problem/Unbounded](https://rosettacode.org/wiki/Knapsack_problem/Unbounded) | 80 | `fractions`, `itertools` |
| [`knights-tour`](tasks/knights-tour/knights-tour.om) | [Knight's tour](https://rosettacode.org/wiki/Knight's_tour) | 125 | plain Python |
| [`kronecker-product`](tasks/kronecker-product/kronecker-product.om) | [Kronecker product](https://rosettacode.org/wiki/Kronecker_product) | 137 | plain Python |
| [`langtons-ant`](tasks/langtons-ant/langtons-ant.om) | [Langton's ant](https://rosettacode.org/wiki/Langton's_ant) | 130 | plain Python |
| [`leap-year`](tasks/leap-year/leap-year.om) | [Leap year](https://rosettacode.org/wiki/Leap_year) | 54 | `calendar` |
| [`least-common-multiple`](tasks/least-common-multiple/least-common-multiple.om) | [Least common multiple](https://rosettacode.org/wiki/Least_common_multiple) | 78 | `functools`, `math` |
| [`letter-frequency`](tasks/letter-frequency/letter-frequency.om) | [Letter frequency](https://rosettacode.org/wiki/Letter_frequency) | 52 | `collections`, `string` |
| [`levenshtein-distance`](tasks/levenshtein-distance/levenshtein-distance.om) | [Levenshtein distance](https://rosettacode.org/wiki/Levenshtein_distance) | 76 | plain Python |
| [`longest-common-prefix`](tasks/longest-common-prefix/longest-common-prefix.om) | [Longest common prefix](https://rosettacode.org/wiki/Longest_common_prefix) | 80 | `os.path` |
| [`longest-common-subsequence`](tasks/longest-common-subsequence/longest-common-subsequence.om) | [Longest common subsequence](https://rosettacode.org/wiki/Longest_common_subsequence) | 72 | plain Python |
| [`longest-increasing-subsequence`](tasks/longest-increasing-subsequence/longest-increasing-subsequence.om) | [Longest increasing subsequence](https://rosettacode.org/wiki/Longest_increasing_subsequence) | 137 | `itertools` |
| [`look-and-say-sequence`](tasks/look-and-say-sequence/look-and-say-sequence.om) | [Look-and-say sequence](https://rosettacode.org/wiki/Look-and-say_sequence) | 63 | `itertools` |
| [`loops-break`](tasks/loops-break/loops-break.om) | [Loops/Break](https://rosettacode.org/wiki/Loops/Break) | 42 | plain Python |
| [`loops-continue`](tasks/loops-continue/loops-continue.om) | [Loops/Continue](https://rosettacode.org/wiki/Loops/Continue) | 39 | plain Python |
| [`loops-do-while`](tasks/loops-do-while/loops-do-while.om) | [Loops/Do-while](https://rosettacode.org/wiki/Loops/Do-while) | 38 | plain Python |
| [`loops-downward-for`](tasks/loops-downward-for/loops-downward-for.om) | [Loops/Downward for](https://rosettacode.org/wiki/Loops/Downward_for) | 33 | plain Python |
| [`loops-for`](tasks/loops-for/loops-for.om) | [Loops/For](https://rosettacode.org/wiki/Loops/For) | 22 | plain Python |
| [`loops-for-with-a-specified-step`](tasks/loops-for-with-a-specified-step/loops-for-with-a-specified-step.om) | [Loops/For with a specified step](https://rosettacode.org/wiki/Loops/For_with_a_specified_step) | 38 | plain Python |
| [`loops-foreach`](tasks/loops-foreach/loops-foreach.om) | [Loops/Foreach](https://rosettacode.org/wiki/Loops/Foreach) | 23 | plain Python |
| [`loops-n-plus-one-half`](tasks/loops-n-plus-one-half/loops-n-plus-one-half.om) | [Loops/N plus one half](https://rosettacode.org/wiki/Loops/N_plus_one_half) | 40 | plain Python |
| [`loops-while`](tasks/loops-while/loops-while.om) | [Loops/While](https://rosettacode.org/wiki/Loops/While) | 35 | plain Python |
| [`lucas-lehmer-test`](tasks/lucas-lehmer-test/lucas-lehmer-test.om) | [Lucas-Lehmer test](https://rosettacode.org/wiki/Lucas-Lehmer_test) | 100 | plain Python |
| [`ludic-numbers`](tasks/ludic-numbers/ludic-numbers.om) | [Ludic numbers](https://rosettacode.org/wiki/Ludic_numbers) | 98 | plain Python |
| [`luhn-test-of-credit-card-numbers`](tasks/luhn-test-of-credit-card-numbers/luhn-test-of-credit-card-numbers.om) | [Luhn test of credit card numbers](https://rosettacode.org/wiki/Luhn_test_of_credit_card_numbers) | 48 | plain Python |
| [`magic-squares-of-odd-order`](tasks/magic-squares-of-odd-order/magic-squares-of-odd-order.om) | [Magic squares of odd order](https://rosettacode.org/wiki/Magic_squares_of_odd_order) | 87 | plain Python |
| [`mandelbrot-set`](tasks/mandelbrot-set/mandelbrot-set.om) | [Mandelbrot set](https://rosettacode.org/wiki/Mandelbrot_set) | 46 | plain Python |
| [`matrix-multiplication`](tasks/matrix-multiplication/matrix-multiplication.om) | [Matrix multiplication](https://rosettacode.org/wiki/Matrix_multiplication) | 103 | plain Python |
| [`matrix-transposition`](tasks/matrix-transposition/matrix-transposition.om) | [Matrix transposition](https://rosettacode.org/wiki/Matrix_transposition) | 85 | plain Python |
| [`matrix-with-two-diagonals`](tasks/matrix-with-two-diagonals/matrix-with-two-diagonals.om) | [Matrix with two diagonals](https://rosettacode.org/wiki/Matrix_with_two_diagonals) | 49 | plain Python |
| [`maximum-triangle-path-sum`](tasks/maximum-triangle-path-sum/maximum-triangle-path-sum.om) | [Maximum triangle path sum](https://rosettacode.org/wiki/Maximum_triangle_path_sum) | 101 | plain Python |
| [`maze-generation`](tasks/maze-generation/maze-generation.om) | [Maze generation](https://rosettacode.org/wiki/Maze_generation) | 148 | plain Python |
| [`maze-solving`](tasks/maze-solving/maze-solving.om) | [Maze solving](https://rosettacode.org/wiki/Maze_solving) | 208 | plain Python |
| [`md5`](tasks/md5/md5.om) | [MD5](https://rosettacode.org/wiki/MD5) | 144 | `hashlib` |
| [`merge-sort`](tasks/merge-sort/merge-sort.om) | [Sorting algorithms/Merge sort](https://rosettacode.org/wiki/Sorting_algorithms/Merge_sort) | 119 | plain Python |
| [`mersenne-primes`](tasks/mersenne-primes/mersenne-primes.om) | [Mersenne primes](https://rosettacode.org/wiki/Mersenne_primes) | 125 | plain Python |
| [`miller-rabin-primality-test`](tasks/miller-rabin-primality-test/miller-rabin-primality-test.om) | [Miller-Rabin primality test](https://rosettacode.org/wiki/Miller-Rabin_primality_test) | 143 | `math` |
| [`mobius-function`](tasks/mobius-function/mobius-function.om) | [Möbius function](https://rosettacode.org/wiki/M%C3%B6bius_function) | 60 | plain Python |
| [`modular-exponentiation`](tasks/modular-exponentiation/modular-exponentiation.om) | [Modular exponentiation](https://rosettacode.org/wiki/Modular_exponentiation) | 113 | plain Python |
| [`modular-inverse`](tasks/modular-inverse/modular-inverse.om) | [Modular inverse](https://rosettacode.org/wiki/Modular_inverse) | 86 | plain Python |
| [`n-queens-problem`](tasks/n-queens-problem/n-queens-problem.om) | [N-queens problem](https://rosettacode.org/wiki/N-queens_problem) | 65 | `itertools` |
| [`narcissistic-decimal-number`](tasks/narcissistic-decimal-number/narcissistic-decimal-number.om) | [Narcissistic decimal number](https://rosettacode.org/wiki/Narcissistic_decimal_number) | 66 | `itertools` |
| [`number-names`](tasks/number-names/number-names.om) | [Number names](https://rosettacode.org/wiki/Number_names) | 120 | plain Python |
| [`one-dimensional-cellular-automata`](tasks/one-dimensional-cellular-automata/one-dimensional-cellular-automata.om) | [One-dimensional cellular automata](https://rosettacode.org/wiki/One-dimensional_cellular_automata) | 88 | plain Python |
| [`ordered-partitions`](tasks/ordered-partitions/ordered-partitions.om) | [Ordered partitions](https://rosettacode.org/wiki/Ordered_partitions) | 107 | `itertools`, `math` |
| [`ordered-words`](tasks/ordered-words/ordered-words.om) | [Ordered words](https://rosettacode.org/wiki/Ordered_words) | 51 | plain Python |
| [`palindrome-detection`](tasks/palindrome-detection/palindrome-detection.om) | [Palindrome detection](https://rosettacode.org/wiki/Palindrome_detection) | 70 | plain Python |
| [`pancake-sort`](tasks/pancake-sort/pancake-sort.om) | [Sorting algorithms/Pancake sort](https://rosettacode.org/wiki/Sorting_algorithms/Pancake_sort) | 116 | plain Python |
| [`pangram-checker`](tasks/pangram-checker/pangram-checker.om) | [Pangram checker](https://rosettacode.org/wiki/Pangram_checker) | 51 | `string` |
| [`pascals-triangle`](tasks/pascals-triangle/pascals-triangle.om) | [Pascal's triangle](https://rosettacode.org/wiki/Pascal's_triangle) | 53 | `math` |
| [`patience-sort`](tasks/patience-sort/patience-sort.om) | [Sorting algorithms/Patience sort](https://rosettacode.org/wiki/Sorting_algorithms/Patience_sort) | 126 | `heapq` |
| [`perfect-numbers`](tasks/perfect-numbers/perfect-numbers.om) | [Perfect numbers](https://rosettacode.org/wiki/Perfect_numbers) | 52 | plain Python |
| [`perfect-totient-numbers`](tasks/perfect-totient-numbers/perfect-totient-numbers.om) | [Perfect totient numbers](https://rosettacode.org/wiki/Perfect_totient_numbers) | 68 | plain Python |
| [`permutation-sort`](tasks/permutation-sort/permutation-sort.om) | [Sorting algorithms/Permutation sort](https://rosettacode.org/wiki/Sorting_algorithms/Permutation_sort) | 145 | `itertools` |
| [`permutations`](tasks/permutations/permutations.om) | [Permutations](https://rosettacode.org/wiki/Permutations) | 83 | plain Python |
| [`permutations-by-swapping`](tasks/permutations-by-swapping/permutations-by-swapping.om) | [Permutations by swapping](https://rosettacode.org/wiki/Permutations_by_swapping) | 101 | plain Python |
| [`permutations-derangements`](tasks/permutations-derangements/permutations-derangements.om) | [Permutations/Derangements](https://rosettacode.org/wiki/Permutations/Derangements) | 144 | `itertools`, `math` |
| [`pernicious-numbers`](tasks/pernicious-numbers/pernicious-numbers.om) | [Pernicious numbers](https://rosettacode.org/wiki/Pernicious_numbers) | 75 | plain Python |
| [`phrase-reversals`](tasks/phrase-reversals/phrase-reversals.om) | [Phrase reversals](https://rosettacode.org/wiki/Phrase_reversals) | 64 | plain Python |
| [`population-count`](tasks/population-count/population-count.om) | [Population count](https://rosettacode.org/wiki/Population_count) | 67 | `itertools` |
| [`power-set`](tasks/power-set/power-set.om) | [Power set](https://rosettacode.org/wiki/Power_set) | 56 | plain Python |
| [`primality-by-trial-division`](tasks/primality-by-trial-division/primality-by-trial-division.om) | [Primality by trial division](https://rosettacode.org/wiki/Primality_by_trial_division) | 74 | `math` |
| [`prime-decomposition`](tasks/prime-decomposition/prime-decomposition.om) | [Prime decomposition](https://rosettacode.org/wiki/Prime_decomposition) | 64 | plain Python |
| [`priority-queue`](tasks/priority-queue/priority-queue.om) | [Priority queue](https://rosettacode.org/wiki/Priority_queue) | 115 | `heapq` |
| [`proper-divisors`](tasks/proper-divisors/proper-divisors.om) | [Proper divisors](https://rosettacode.org/wiki/Proper_divisors) | 69 | `math` |
| [`pythagorean-triples`](tasks/pythagorean-triples/pythagorean-triples.om) | [Pythagorean triples](https://rosettacode.org/wiki/Pythagorean_triples) | 78 | `math` |
| [`queue-definition`](tasks/queue-definition/queue-definition.om) | [Queue/Definition](https://rosettacode.org/wiki/Queue/Definition) | 97 | `collections` |
| [`queue-usage`](tasks/queue-usage/queue-usage.om) | [Queue/Usage](https://rosettacode.org/wiki/Queue/Usage) | 95 | plain Python |
| [`quicksort`](tasks/quicksort/quicksort.om) | [Sorting algorithms/Quicksort](https://rosettacode.org/wiki/Sorting_algorithms/Quicksort) | 105 | plain Python |
| [`radix-sort`](tasks/radix-sort/radix-sort.om) | [Sorting algorithms/Radix sort](https://rosettacode.org/wiki/Sorting_algorithms/Radix_sort) | 133 | plain Python |
| [`recamans-sequence`](tasks/recamans-sequence/recamans-sequence.om) | [Recaman's sequence](https://rosettacode.org/wiki/Recaman%27s_sequence) | 76 | plain Python |
| [`remove-duplicate-elements`](tasks/remove-duplicate-elements/remove-duplicate-elements.om) | [Remove duplicate elements](https://rosettacode.org/wiki/Remove_duplicate_elements) | 102 | plain Python |
| [`remove-vowels-from-a-string`](tasks/remove-vowels-from-a-string/remove-vowels-from-a-string.om) | [Remove vowels from a string](https://rosettacode.org/wiki/Remove_vowels_from_a_string) | 39 | plain Python |
| [`repeat-a-string`](tasks/repeat-a-string/repeat-a-string.om) | [Repeat a string](https://rosettacode.org/wiki/Repeat_a_string) | 31 | plain Python |
| [`reverse-a-string`](tasks/reverse-a-string/reverse-a-string.om) | [Reverse a string](https://rosettacode.org/wiki/Reverse_a_string) | 28 | plain Python |
| [`reverse-words-in-a-string`](tasks/reverse-words-in-a-string/reverse-words-in-a-string.om) | [Reverse words in a string](https://rosettacode.org/wiki/Reverse_words_in_a_string) | 55 | plain Python |
| [`roman-numerals-encode`](tasks/roman-numerals-encode/roman-numerals-encode.om) | [Roman numerals/Encode](https://rosettacode.org/wiki/Roman_numerals/Encode) | 70 | plain Python |
| [`rot-13`](tasks/rot-13/rot-13.om) | [Rot-13](https://rosettacode.org/wiki/Rot-13) | 35 | `codecs` |
| [`run-length-encoding`](tasks/run-length-encoding/run-length-encoding.om) | [Run-length encoding](https://rosettacode.org/wiki/Run-length_encoding) | 79 | `itertools`, `re` |
| [`selection-sort`](tasks/selection-sort/selection-sort.om) | [Sorting algorithms/Selection sort](https://rosettacode.org/wiki/Sorting_algorithms/Selection_sort) | 98 | plain Python |
| [`semiprime`](tasks/semiprime/semiprime.om) | [Semiprime](https://rosettacode.org/wiki/Semiprime) | 79 | plain Python |
| [`sha-1`](tasks/sha-1/sha-1.om) | [SHA-1](https://rosettacode.org/wiki/SHA-1) | 131 | `hashlib` |
| [`sha-256`](tasks/sha-256/sha-256.om) | [SHA-256](https://rosettacode.org/wiki/SHA-256) | 208 | `hashlib` |
| [`shell-sort`](tasks/shell-sort/shell-sort.om) | [Sorting algorithms/Shell sort](https://rosettacode.org/wiki/Sorting_algorithms/Shell_sort) | 103 | plain Python |
| [`sieve-of-eratosthenes`](tasks/sieve-of-eratosthenes/sieve-of-eratosthenes.om) | [Sieve of Eratosthenes](https://rosettacode.org/wiki/Sieve_of_Eratosthenes) | 48 | plain Python |
| [`smith-numbers`](tasks/smith-numbers/smith-numbers.om) | [Smith numbers](https://rosettacode.org/wiki/Smith_numbers) | 89 | plain Python |
| [`sort-an-integer-array`](tasks/sort-an-integer-array/sort-an-integer-array.om) | [Sort an integer array](https://rosettacode.org/wiki/Sort_an_integer_array) | 104 | plain Python |
| [`sort-disjoint-sublist`](tasks/sort-disjoint-sublist/sort-disjoint-sublist.om) | [Sort disjoint sublist](https://rosettacode.org/wiki/Sort_disjoint_sublist) | 124 | plain Python |
| [`sort-three-variables`](tasks/sort-three-variables/sort-three-variables.om) | [Sort three variables](https://rosettacode.org/wiki/Sort_three_variables) | 162 | plain Python |
| [`soundex`](tasks/soundex/soundex.om) | [Soundex](https://rosettacode.org/wiki/Soundex) | 73 | plain Python |
| [`spiral-matrix`](tasks/spiral-matrix/spiral-matrix.om) | [Spiral matrix](https://rosettacode.org/wiki/Spiral_matrix) | 91 | plain Python |
| [`square-free-integers`](tasks/square-free-integers/square-free-integers.om) | [Square-free integers](https://rosettacode.org/wiki/Square-free_integers) | 98 | `math` |
| [`stack`](tasks/stack/stack.om) | [Stack](https://rosettacode.org/wiki/Stack) | 102 | plain Python |
| [`stern-brocot-sequence`](tasks/stern-brocot-sequence/stern-brocot-sequence.om) | [Stern-Brocot sequence](https://rosettacode.org/wiki/Stern-Brocot_sequence) | 97 | `math` |
| [`stooge-sort`](tasks/stooge-sort/stooge-sort.om) | [Sorting algorithms/Stooge sort](https://rosettacode.org/wiki/Sorting_algorithms/Stooge_sort) | 97 | plain Python |
| [`strand-sort`](tasks/strand-sort/strand-sort.om) | [Sorting algorithms/Strand sort](https://rosettacode.org/wiki/Sorting_algorithms/Strand_sort) | 155 | plain Python |
| [`string-append`](tasks/string-append/string-append.om) | [String append](https://rosettacode.org/wiki/String_append) | 28 | plain Python |
| [`string-case`](tasks/string-case/string-case.om) | [String case](https://rosettacode.org/wiki/String_case) | 37 | plain Python |
| [`string-comparison`](tasks/string-comparison/string-comparison.om) | [String comparison](https://rosettacode.org/wiki/String_comparison) | 83 | plain Python |
| [`string-concatenation`](tasks/string-concatenation/string-concatenation.om) | [String concatenation](https://rosettacode.org/wiki/String_concatenation) | 30 | plain Python |
| [`string-length`](tasks/string-length/string-length.om) | [String length](https://rosettacode.org/wiki/String_length) | 51 | `sys` |
| [`string-matching`](tasks/string-matching/string-matching.om) | [String matching](https://rosettacode.org/wiki/String_matching) | 69 | plain Python |
| [`string-prepend`](tasks/string-prepend/string-prepend.om) | [String prepend](https://rosettacode.org/wiki/String_prepend) | 37 | plain Python |
| [`strip-a-set-of-characters-from-a-string`](tasks/strip-a-set-of-characters-from-a-string/strip-a-set-of-characters-from-a-string.om) | [Strip a set of characters from a string](https://rosettacode.org/wiki/Strip_a_set_of_characters_from_a_string) | 38 | plain Python |
| [`strip-comments-from-a-string`](tasks/strip-comments-from-a-string/strip-comments-from-a-string.om) | [Strip comments from a string](https://rosettacode.org/wiki/Strip_comments_from_a_string) | 51 | `re` |
| [`strip-whitespace-from-a-string`](tasks/strip-whitespace-from-a-string/strip-whitespace-from-a-string.om) | [Strip whitespace from a string/Top and tail](https://rosettacode.org/wiki/Strip_whitespace_from_a_string/Top_and_tail) | 49 | plain Python |
| [`substitution-cipher`](tasks/substitution-cipher/substitution-cipher.om) | [Substitution cipher](https://rosettacode.org/wiki/Substitution_cipher) | 50 | `string` |
| [`substring`](tasks/substring/substring.om) | [Substring](https://rosettacode.org/wiki/Substring) | 43 | plain Python |
| [`sudoku`](tasks/sudoku/sudoku.om) | [Sudoku](https://rosettacode.org/wiki/Sudoku) | 103 | plain Python |
| [`sum-and-product-of-an-array`](tasks/sum-and-product-of-an-array/sum-and-product-of-an-array.om) | [Sum and product of an array](https://rosettacode.org/wiki/Sum_and_product_of_an_array) | 47 | `math` |
| [`sum-digits-of-an-integer`](tasks/sum-digits-of-an-integer/sum-digits-of-an-integer.om) | [Sum digits of an integer](https://rosettacode.org/wiki/Sum_digits_of_an_integer) | 76 | `string` |
| [`sum-multiples-of-3-and-5`](tasks/sum-multiples-of-3-and-5/sum-multiples-of-3-and-5.om) | [Sum multiples of 3 and 5](https://rosettacode.org/wiki/Sum_multiples_of_3_and_5) | 54 | plain Python |
| [`temperature-conversion`](tasks/temperature-conversion/temperature-conversion.om) | [Temperature conversion](https://rosettacode.org/wiki/Temperature_conversion) | 71 | `fractions` |
| [`the-twelve-days-of-christmas`](tasks/the-twelve-days-of-christmas/the-twelve-days-of-christmas.om) | [The Twelve Days of Christmas](https://rosettacode.org/wiki/The_Twelve_Days_of_Christmas) | 55 | plain Python |
| [`thue-morse`](tasks/thue-morse/thue-morse.om) | [Thue-Morse](https://rosettacode.org/wiki/Thue-Morse) | 33 | plain Python |
| [`tokenize-a-string`](tasks/tokenize-a-string/tokenize-a-string.om) | [Tokenize a string](https://rosettacode.org/wiki/Tokenize_a_string) | 36 | plain Python |
| [`topological-sort`](tasks/topological-sort/topological-sort.om) | [Topological sort](https://rosettacode.org/wiki/Topological_sort) | 149 | `heapq` |
| [`topswops`](tasks/topswops/topswops.om) | [Topswops](https://rosettacode.org/wiki/Topswops) | 121 | `itertools` |
| [`totient-function`](tasks/totient-function/totient-function.om) | [Totient function](https://rosettacode.org/wiki/Totient_function) | 79 | `math` |
| [`towers-of-hanoi`](tasks/towers-of-hanoi/towers-of-hanoi.om) | [Towers of Hanoi](https://rosettacode.org/wiki/Towers_of_Hanoi) | 47 | plain Python |
| [`tree-traversal`](tasks/tree-traversal/tree-traversal.om) | [Tree traversal](https://rosettacode.org/wiki/Tree_traversal) | 105 | `collections` |
| [`twin-primes`](tasks/twin-primes/twin-primes.om) | [Twin primes](https://rosettacode.org/wiki/Twin_primes) | 79 | `bisect`, `itertools` |
| [`url-decoding`](tasks/url-decoding/url-decoding.om) | [URL decoding](https://rosettacode.org/wiki/URL_decoding) | 51 | `sys`, `urllib.parse` |
| [`url-encoding`](tasks/url-encoding/url-encoding.om) | [URL encoding](https://rosettacode.org/wiki/URL_encoding) | 50 | `urllib.parse` |
| [`van-eck-sequence`](tasks/van-eck-sequence/van-eck-sequence.om) | [Van Eck sequence](https://rosettacode.org/wiki/Van_Eck_sequence) | 54 | plain Python |
| [`vigenere-cipher`](tasks/vigenere-cipher/vigenere-cipher.om) | [Vigenère cipher](https://rosettacode.org/wiki/Vigen%C3%A8re_cipher) | 55 | plain Python |
| [`water-collected-between-towers`](tasks/water-collected-between-towers/water-collected-between-towers.om) | [Water collected between towers](https://rosettacode.org/wiki/Water_collected_between_towers) | 146 | plain Python |
| [`wireworld`](tasks/wireworld/wireworld.om) | [Wireworld](https://rosettacode.org/wiki/Wireworld) | 96 | plain Python |
| [`word-wrap`](tasks/word-wrap/word-wrap.om) | [Word wrap](https://rosettacode.org/wiki/Word_wrap) | 53 | `textwrap` |
| [`zig-zag-matrix`](tasks/zig-zag-matrix/zig-zag-matrix.om) | [Zig-zag matrix](https://rosettacode.org/wiki/Zig-zag_matrix) | 77 | plain Python |

The SHA-256 round constants and initial values in `tasks/sha-256/sha-256.om` were copied
mechanically from omega-mv's [`om/sha256/sha256-om2.om`](https://github.com/aien-dev/omega-mv/blob/e5b32567a7aff3ce594e3254a622a846a6cd190b/om/sha256/sha256-om2.om); the hashes
are checked against Python's `hashlib`, and "Rosetta code" gives Rosetta Code's published value
`764faf5c…cdfcf`.

The 49 number-theory tasks that carry a `wolfram.txt` were also checked a second, independent way:
the file records a Wolfram Language query that rebuilds the whole expected output from Wolfram
built-ins, and whether that text's SHA-256 matched `expected.txt` (all 49 record a match).

## Exercises

47 small problems in the Exercism style. Each `exercises/<name>/<name>.om` is a stub that traps
until you write the function; `test.om` holds the cases. For 42 of them the cases come from
[exercism/problem-specifications](https://github.com/exercism/problem-specifications)
`canonical-data.json` at commit `650bebeb` (MIT; see [NOTICE](NOTICE)); each `test.om` notes every
case's uuid and how many cases it kept, skipped and left out as superseded.

```sh
sh run.sh                              # once, to birth omc into build/
sh exercise.sh exercises/leap          # test your exercises/leap/leap.om
```

Omega has no imports, so `exercise.sh` joins your file and `test.om` into one unit, compiles it and
runs it. You get one `ok N - ...` or `not ok N - ...` line per case and `EXERCISE PASS <name>` when
all pass. Reference solutions are in `exercises/<name>/.meta/example.om`.

| Stub | Problem |
| --- | --- |
| [`acronym`](exercises/acronym/acronym.om) | [acronym](https://exercism.org/tracks/python/exercises/acronym) |
| [`all-your-base`](exercises/all-your-base/all-your-base.om) | [all-your-base](https://exercism.org/tracks/python/exercises/all-your-base) |
| [`allergies`](exercises/allergies/allergies.om) | [allergies](https://exercism.org/tracks/python/exercises/allergies) |
| [`armstrong-numbers`](exercises/armstrong-numbers/armstrong-numbers.om) | [armstrong-numbers](https://exercism.org/tracks/python/exercises/armstrong-numbers) |
| [`atbash-cipher`](exercises/atbash-cipher/atbash-cipher.om) | [atbash-cipher](https://exercism.org/tracks/python/exercises/atbash-cipher) |
| [`binary-search`](exercises/binary-search/binary-search.om) | [binary-search](https://exercism.org/tracks/python/exercises/binary-search) |
| [`bob`](exercises/bob/bob.om) | [bob](https://exercism.org/tracks/python/exercises/bob) |
| [`change`](exercises/change/change.om) | [change](https://exercism.org/tracks/python/exercises/change) |
| [`collatz-conjecture`](exercises/collatz-conjecture/collatz-conjecture.om) | [collatz-conjecture](https://exercism.org/tracks/python/exercises/collatz-conjecture) |
| [`darts`](exercises/darts/darts.om) | [darts](https://exercism.org/tracks/python/exercises/darts) |
| [`difference-of-squares`](exercises/difference-of-squares/difference-of-squares.om) | [difference-of-squares](https://exercism.org/tracks/python/exercises/difference-of-squares) |
| [`eliuds-eggs`](exercises/eliuds-eggs/eliuds-eggs.om) | [eliuds-eggs](https://exercism.org/tracks/python/exercises/eliuds-eggs) |
| [`grains`](exercises/grains/grains.om) | [grains](https://exercism.org/tracks/python/exercises/grains) |
| [`hamming`](exercises/hamming/hamming.om) | [hamming](https://exercism.org/tracks/python/exercises/hamming) |
| [`hello-world`](exercises/hello-world/hello-world.om) | [hello-world](https://exercism.org/tracks/python/exercises/hello-world) |
| [`isbn-verifier`](exercises/isbn-verifier/isbn-verifier.om) | [isbn-verifier](https://exercism.org/tracks/python/exercises/isbn-verifier) |
| [`isogram`](exercises/isogram/isogram.om) | [isogram](https://exercism.org/tracks/python/exercises/isogram) |
| [`knapsack`](exercises/knapsack/knapsack.om) | [knapsack](https://exercism.org/tracks/python/exercises/knapsack) |
| [`largest-series-product`](exercises/largest-series-product/largest-series-product.om) | [largest-series-product](https://exercism.org/tracks/python/exercises/largest-series-product) |
| [`leap`](exercises/leap/leap.om) | [leap](https://exercism.org/tracks/python/exercises/leap) |
| [`luhn`](exercises/luhn/luhn.om) | [luhn](https://exercism.org/tracks/python/exercises/luhn) |
| [`nth-prime`](exercises/nth-prime/nth-prime.om) | [nth-prime](https://exercism.org/tracks/python/exercises/nth-prime) |
| [`nucleotide-count`](exercises/nucleotide-count/nucleotide-count.om) | [nucleotide-count](https://exercism.org/tracks/python/exercises/nucleotide-count) |
| [`pangram`](exercises/pangram/pangram.om) | [pangram](https://exercism.org/tracks/python/exercises/pangram) |
| [`pascals-triangle`](exercises/pascals-triangle/pascals-triangle.om) | [pascals-triangle](https://exercism.org/tracks/python/exercises/pascals-triangle) |
| [`perfect-numbers`](exercises/perfect-numbers/perfect-numbers.om) | [perfect-numbers](https://exercism.org/tracks/python/exercises/perfect-numbers) |
| [`prime-factors`](exercises/prime-factors/prime-factors.om) | [prime-factors](https://exercism.org/tracks/python/exercises/prime-factors) |
| [`protein-translation`](exercises/protein-translation/protein-translation.om) | [protein-translation](https://exercism.org/tracks/python/exercises/protein-translation) |
| [`queen-attack`](exercises/queen-attack/queen-attack.om) | [queen-attack](https://exercism.org/tracks/python/exercises/queen-attack) |
| [`raindrops`](exercises/raindrops/raindrops.om) | [raindrops](https://exercism.org/tracks/python/exercises/raindrops) |
| [`resistor-color`](exercises/resistor-color/resistor-color.om) | [resistor-color](https://exercism.org/tracks/python/exercises/resistor-color) |
| [`resistor-color-duo`](exercises/resistor-color-duo/resistor-color-duo.om) | [resistor-color-duo](https://exercism.org/tracks/python/exercises/resistor-color-duo) |
| [`resistor-color-trio`](exercises/resistor-color-trio/resistor-color-trio.om) | [resistor-color-trio](https://exercism.org/tracks/python/exercises/resistor-color-trio) |
| [`reverse-string`](exercises/reverse-string/reverse-string.om) | [reverse-string](https://exercism.org/tracks/python/exercises/reverse-string) |
| [`rna-transcription`](exercises/rna-transcription/rna-transcription.om) | [rna-transcription](https://exercism.org/tracks/python/exercises/rna-transcription) |
| [`rotational-cipher`](exercises/rotational-cipher/rotational-cipher.om) | [rotational-cipher](https://exercism.org/tracks/python/exercises/rotational-cipher) |
| [`run-length-encoding`](exercises/run-length-encoding/run-length-encoding.om) | [run-length-encoding](https://exercism.org/tracks/python/exercises/run-length-encoding) |
| [`saddle-points`](exercises/saddle-points/saddle-points.om) | [saddle-points](https://exercism.org/tracks/python/exercises/saddle-points) |
| [`scrabble-score`](exercises/scrabble-score/scrabble-score.om) | [scrabble-score](https://exercism.org/tracks/python/exercises/scrabble-score) |
| [`secret-handshake`](exercises/secret-handshake/secret-handshake.om) | [secret-handshake](https://exercism.org/tracks/python/exercises/secret-handshake) |
| [`series`](exercises/series/series.om) | [series](https://exercism.org/tracks/python/exercises/series) |
| [`sieve`](exercises/sieve/sieve.om) | [sieve](https://exercism.org/tracks/python/exercises/sieve) |
| [`space-age`](exercises/space-age/space-age.om) | [space-age](https://exercism.org/tracks/python/exercises/space-age) |
| [`square-root`](exercises/square-root/square-root.om) | [square-root](https://exercism.org/tracks/python/exercises/square-root) |
| [`sum-of-multiples`](exercises/sum-of-multiples/sum-of-multiples.om) | [sum-of-multiples](https://exercism.org/tracks/python/exercises/sum-of-multiples) |
| [`triangle`](exercises/triangle/triangle.om) | [triangle](https://exercism.org/tracks/python/exercises/triangle) |
| [`two-fer`](exercises/two-fer/two-fer.om) | [two-fer](https://exercism.org/tracks/python/exercises/two-fer) |

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
