# Independent reference for "Remove duplicate elements" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
a = [4, 9, 4, 1, -3, 9, 0, 1, 7, 4, -3, 12, 0, 9, 5]
print(*a)
print(*dict.fromkeys(a))
