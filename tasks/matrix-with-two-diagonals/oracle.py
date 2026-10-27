# Independent reference for "Matrix with two diagonals" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for k, n in enumerate((6, 7)):
    if k:
        print()
    for i in range(n):
        row = ["0"] * n
        row[i] = row[n - 1 - i] = "1"
        print(" ".join(row))
