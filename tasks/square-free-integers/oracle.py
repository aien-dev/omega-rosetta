# Independent reference for "Square-free integers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
def squarefree(n):
    m, p = n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return False
        p += 1
    return True
print("square-free integers from 1 to 145: " + " ".join(str(n) for n in range(1, 146) if squarefree(n)))
B = 10 ** 12
print(f"square-free integers from {B} to {B + 145}: " + " ".join(str(n) for n in range(B, B + 146) if squarefree(n)))
# counts by the Moebius formula: Q(x) = sum mu(d) * floor(x / d^2)
N = 1000
mu = [1] * (N + 1)
isp = [True] * (N + 1)
for p in range(2, N + 1):
    if isp[p]:
        for j in range(p, N + 1, p):
            if j > p:
                isp[j] = False
            mu[j] = -mu[j]
        for j in range(p * p, N + 1, p * p):
            mu[j] = 0
for e in range(2, 7):
    x = 10 ** e
    print(f"square-free integers up to {x}: {sum(mu[d] * (x // (d * d)) for d in range(1, math.isqrt(x) + 1))}")
