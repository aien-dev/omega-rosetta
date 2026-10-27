# Independent reference for "Perfect numbers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for n in range(2, 10000):
    if sum(d for d in range(1, n) if n % d == 0) == n:
        print(n)
