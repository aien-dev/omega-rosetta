# Independent reference for "Matrix multiplication" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def matmul(a, b):
    # each entry as a dot product of a row of a with a column of b (zip(*b) gives the columns)
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]
def show(m):
    for row in m:
        print("".join(f"{v:5}" for v in row))
cases = [([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]),
         ([[3 * i - 10 for i in range(r * 3, r * 3 + 3)] for r in range(3)],
          [[4 - (5 * i) % 7 for i in range(r * 3, r * 3 + 3)] for r in range(3)])]
for n, (a, b) in enumerate(cases):
    if n:
        print()
    show(a); print("times"); show(b); print("equals"); show(matmul(a, b))
