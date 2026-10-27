# Independent reference for "Miller-Rabin primality test" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
def prime(n):
    # trial division for small n; for large n, a strong-pseudoprime test with every prime base below 40
    if n < 2:
        return False
    if n < 10**6:
        return all(n % d for d in range(2, math.isqrt(n) + 1))
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % a == 0:
            return False
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True
print("primes below 100: " + " ".join(str(n) for n in range(100) if prime(n)))
for n in [561, 1105, 1729, 2047, 3215031751, 2147483647, 3825123056546413051, 4611686018427387903,
          2305843009213693951, 9223372036854775783, 18446744073709551557, 18446744073709551615]:
    print(f"{n}: {'prime' if prime(n) else 'composite'}")
