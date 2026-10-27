# Independent reference for "Anti-primes" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
out, best, n = [], 0, 0
while len(out) < 20:
    n += 1
    k = sum(1 for d in range(1, n + 1) if n % d == 0)
    if k > best:
        best = k
        out.append(n)
print("first 20 anti-primes: " + " ".join(map(str, out)))
