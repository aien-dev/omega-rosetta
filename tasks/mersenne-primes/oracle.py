# Independent reference for "Mersenne primes" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# Lucas-Lehmer with Python integers (p = 2 by definition), a different test from the Omega program's Miller-Rabin
def mersenne_prime(p):
    if p == 2:
        return True
    if any(p % d == 0 for d in range(2, p)):
        return False
    m, s = (1 << p) - 1, 4
    for _ in range(p - 2):
        s = (s * s - 2) % m
    return s == 0
for p in range(2, 64):
    if mersenne_prime(p):
        print(f"2^{p} - 1 = {(1 << p) - 1}")
