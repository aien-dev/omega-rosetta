# Independent reference for "Sieve of Eratosthenes" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
N = 1000
print(" ".join(str(n) for n in range(2, N + 1) if all(n % d for d in range(2, int(n ** 0.5) + 1))))
