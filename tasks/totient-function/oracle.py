# Independent reference for "Totient function" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
for n in range(1, 26):
    phi = sum(1 for k in range(1, n + 1) if math.gcd(n, k) == 1)
    print(f"phi({n}) = {phi}" + (", prime" if phi == n - 1 else ""))
N = 100000
s = bytearray([1]) * (N + 1)
s[0] = s[1] = 0
for i in range(2, math.isqrt(N) + 1):
    if s[i]:
        s[i * i::i] = bytes(len(range(i * i, N + 1, i)))
for lim in [100, 1000, 10000, 100000]:
    print(f"primes up to {lim}: {sum(s[:lim + 1])}")
