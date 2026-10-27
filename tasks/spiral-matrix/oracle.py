# Independent reference for "Spiral matrix" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# peel the outer ring and recurse on the inner square: ring numbers go right, down, left, up
def spiral(n):
    m = [[0] * n for _ in range(n)]
    k = 0
    for layer in range((n + 1) // 2):
        lo, hi = layer, n - 1 - layer
        if lo == hi:
            m[lo][lo] = k
            break
        cells = ([(lo, c) for c in range(lo, hi)] + [(r, hi) for r in range(lo, hi)] +
                 [(hi, c) for c in range(hi, lo, -1)] + [(r, lo) for r in range(hi, lo, -1)])
        for r, c in cells:
            m[r][c] = k
            k += 1
    return m
for i, n in enumerate((5, 8)):
    if i:
        print()
    for row in spiral(n):
        print("".join(f"{v:3}" for v in row))
