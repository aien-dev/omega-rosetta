# Independent reference for "Lucas-Lehmer test" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# the exponents p <= 63 for which 2^p - 1 has no divisor up to its square root, by trial division over
# 2kp + 1, the only form a divisor of 2^p - 1 can take for prime p (a different method from Lucas-Lehmer)
def mersenne_prime(p):
    if p < 2 or any(p % d == 0 for d in range(2, p)):
        return False
    m = (1 << p) - 1
    q = 2 * p + 1
    while q * q <= m:
        if m % q == 0:
            return False
        q += 2 * p
    return True
print("Mersenne primes 2^p - 1 for p <= 63, by the Lucas-Lehmer test:")
print(" ".join(f"M{p}" for p in range(2, 64) if mersenne_prime(p)))
