# Independent reference for "Magic squares of odd order" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# Cross-check, WolframLanguageEvaluator: Table[n (n^2 + 1)/2, {n, {3, 5, 9}}] -> {15, 65, 369}
# the cells are kept in a dict keyed by (row, column) on a torus, and the result is checked: every row,
# column and both diagonals must sum to the magic constant
def siamese(n):
    m = {}
    r, c = 0, n // 2
    for k in range(1, n * n + 1):
        m[r, c] = k
        nxt = ((r - 1) % n, (c + 1) % n)
        r, c = ((r + 1) % n, c) if nxt in m else nxt
    return [[m[i, j] for j in range(n)] for i in range(n)]
for t, n in enumerate((3, 5, 9)):
    if t:
        print()
    sq = siamese(n)
    s = n * (n * n + 1) // 2
    assert all(sum(row) == s for row in sq) and all(sum(col) == s for col in zip(*sq))
    assert sum(sq[i][i] for i in range(n)) == s == sum(sq[i][n - 1 - i] for i in range(n))
    for row in sq:
        print("".join(f"{v:4}" for v in row))
    print("magic constant:", s)
