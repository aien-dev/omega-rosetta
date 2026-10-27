# Independent reference for "Array concatenation" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
a = [1, 2, 3]
b = [4, 5, 6, 7]
print(" ".join(map(str, a + b)))
