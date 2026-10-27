# Independent reference for "Determinant and permanent" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# Cross-check, WolframLanguageEvaluator: ms = {the four matrices}; {Map[Det, ms], Map[Permanent, ms]}
#   -> {{-2, -360, 0, 0}, {10, 900, 29556, 6778800}}
from fractions import Fraction
def det(m):
    # Gaussian elimination over exact fractions
    a = [[Fraction(v) for v in row] for row in m]
    n, d = len(a), Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if a[r][c] != 0), None)
        if p is None:
            return 0
        if p != c:
            a[c], a[p] = a[p], a[c]
            d = -d
        d *= a[c][c]
        for r in range(c + 1, n):
            f = a[r][c] / a[c][c]
            a[r] = [x - f * y for x, y in zip(a[r], a[c])]
    return int(d)
def per(m):
    # Ryser's formula: sum over column subsets S of (-1)^(n-|S|) * prod over rows of the sum over S
    n, total = len(m), 0
    for s in range(1, 1 << n):
        cols = [j for j in range(n) if s >> j & 1]
        prod = 1
        for row in m:
            prod *= sum(row[j] for j in cols)
        total += (-1) ** (n - len(cols)) * prod
    return total
cases = [[[1, 2], [3, 4]], [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
         [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [10, 11, 12, 13]],
         [[r * 5 + c for c in range(5)] for r in range(5)]]
for m in cases:
    print("matrix:")
    for row in m:
        print("".join(f"{v:4}" for v in row))
    print("determinant:", det(m))
    print("permanent:", per(m))
