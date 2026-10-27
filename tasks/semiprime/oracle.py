# Independent reference for "Semiprime" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
N = 10000
sieve = [False, False] + [True] * (N - 2)
for i in range(2, 100):
    if sieve[i]:
        sieve[i * i::i] = [False] * len(sieve[i * i::i])
primes = [p for p in range(N) if sieve[p]]
semi = set(p * q for i, p in enumerate(primes) for q in primes[i:] if p * q < N)
print("semiprimes below 100: " + " ".join(str(n) for n in sorted(semi) if n < 100))
print(f"semiprimes below 10000: {len(semi)}")
print("1679 = 23 * 73 is semiprime: " + ("yes" if 1679 in semi else "no"))
