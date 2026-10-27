# Independent reference for "Matrix transposition" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
m = [[i * i - 50 for i in range(r * 5, r * 5 + 5)] for r in range(3)]
for row in m:
    print("".join(f"{v:4}" for v in row))
print("transposed:")
for row in zip(*m):
    print("".join(f"{v:4}" for v in row))
