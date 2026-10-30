# Independent reference for "Copy a string" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
src = "Hello"
dst = list(src)   # an independent copy
dst[0] = "J"
print("source: " + src)
print("copy:   " + "".join(dst))
