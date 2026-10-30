# Independent reference for "Kronecker product" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def kron(a, b):
    # block form: each entry of a scales a whole copy of b
    out = []
    for arow in a:
        for brow in b:
            out.append([x * y for x in arow for y in brow])
    return out
cases = [([[1, 2], [3, 4]], [[0, 5], [6, 7]]),
         ([[0, 1, 0], [1, 1, 1], [0, 1, 0]], [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]])]
for k, (a, b) in enumerate(cases):
    if k:
        print()
    for row in kron(a, b):
        print("".join(f"{v:3}" for v in row))
