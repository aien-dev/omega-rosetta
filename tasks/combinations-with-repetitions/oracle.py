# Independent reference for "Combinations with repetitions" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# Cross-check, WolframLanguageEvaluator: {Binomial[3 + 2 - 1, 2], Binomial[10 + 3 - 1, 3]} -> {6, 220}
from itertools import product
from math import comb
kinds = ["iced", "jam", "plain"]
# all ordered pairs, keeping those already in non-decreasing order
for a, b in product(range(3), repeat=2):
    if a <= b:
        print(kinds[a], kinds[b])
n = sum(1 for t in product(range(10), repeat=3) if t[0] <= t[1] <= t[2])
assert n == comb(10 + 3 - 1, 3)
print("choices of 3 from 10 kinds:", n)
