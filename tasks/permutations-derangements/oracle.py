# Independent reference for "Permutations/Derangements" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# Cross-check, WolframLanguageEvaluator: Table[Subfactorial[n], {n, 0, 9}] and Subfactorial[20]
#   -> {1, 0, 1, 2, 9, 44, 265, 1854, 14833, 133496} and 895014631192902121
from itertools import permutations
from math import factorial
def subfact(n):
    # inclusion-exclusion: sum over k of (-1)^k n!/k!
    return sum((-1) ** k * factorial(n) // factorial(k) for k in range(n + 1))
print("derangements of 0 1 2 3:")
for p in permutations(range(4)):
    if all(p[i] != i for i in range(4)):
        print(*p)
print("n  counted  !n")
for n in range(10):
    counted = sum(1 for p in permutations(range(n)) if all(p[i] != i for i in range(n)))
    print(f"{n} {counted:8}  {subfact(n)}")
print("!20 =", subfact(20))
