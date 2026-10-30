# Independent reference for "Amicable pairs" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
def sigma_proper(n):
    if n < 2:
        return 0
    s = 1
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            s += d + (n // d if n // d != d else 0)
    return s
for n in range(1, 20000):
    m = sigma_proper(n)
    if n < m < 20000 and sigma_proper(m) == n:
        print(n, m)
