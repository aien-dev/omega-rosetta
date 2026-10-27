# Independent reference for "Binary digits" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for n in [0, 5, 50, 9000, 2**64 - 1]:
    print(format(n, "b"))
