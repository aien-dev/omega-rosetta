# Independent reference for "Zig-zag matrix" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# sort the cells by (diagonal, position along it in the direction of travel)
def zigzag(n):
    cells = sorted(((i, j) for i in range(n) for j in range(n)),
                   key=lambda p: (p[0] + p[1], -p[0] if (p[0] + p[1]) % 2 == 0 else p[0]))
    m = [[0] * n for _ in range(n)]
    for k, (i, j) in enumerate(cells):
        m[i][j] = k
    return m
for t, n in enumerate((5, 6)):
    if t:
        print()
    for row in zigzag(n):
        print("".join(f"{v:3}" for v in row))
