# Independent reference for "Fibonacci sequence" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
a, b = 0, 1
for _ in range(94):
    print(a)
    a, b = b, a + b
