# Independent reference for "Identity matrix" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for k, n in enumerate((1, 3, 6)):
    if k:
        print()
    rows = [[0] * n for _ in range(n)]
    for i in range(n):
        rows[i][i] = 1
    for r in rows:
        print(*r)
