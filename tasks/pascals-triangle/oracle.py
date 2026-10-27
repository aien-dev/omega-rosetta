# Independent reference for "Pascal's triangle" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# Cross-check, WolframLanguageEvaluator: Table[Binomial[n, k], {n, 0, 9}, {k, 0, n}]
#   -> {{1}, {1, 1}, {1, 2, 1}, {1, 3, 3, 1}, {1, 4, 6, 4, 1}, {1, 5, 10, 10, 5, 1},
#       {1, 6, 15, 20, 15, 6, 1}, {1, 7, 21, 35, 35, 21, 7, 1}, {1, 8, 28, 56, 70, 56, 28, 8, 1},
#       {1, 9, 36, 84, 126, 126, 84, 36, 9, 1}}
from math import comb
n = 10
for r in range(n):
    print(" " * (2 * (n - r - 1)) + " ".join(str(comb(r, k)) for k in range(r + 1)))
