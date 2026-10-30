# Independent reference for "Pernicious numbers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61}
def pern(n):
    return bin(n).count("1") in PRIMES
out, n = [], 0
while len(out) < 25:
    n += 1
    if pern(n):
        out.append(n)
print("first 25 pernicious numbers: " + " ".join(map(str, out)))
print("pernicious numbers from 888888877 to 888888888: " + " ".join(str(n) for n in range(888888877, 888888889) if pern(n)))
