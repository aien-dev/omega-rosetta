# Independent reference for "Abundant, deficient and perfect number classifications" (Python 3, standard library only).
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
c = {"deficient": 0, "perfect": 0, "abundant": 0}
for n in range(1, 20001):
    s = sigma_proper(n)
    c["deficient" if s < n else "perfect" if s == n else "abundant"] += 1
print(f"deficient: {c['deficient']}")
print(f"perfect:   {c['perfect']}")
print(f"abundant:  {c['abundant']}")
