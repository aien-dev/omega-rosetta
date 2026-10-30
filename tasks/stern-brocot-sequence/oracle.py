# Independent reference for "Stern-Brocot sequence" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
from math import gcd
# Stern's diatomic recurrence: a(1) = 1, a(2n) = a(n), a(2n+1) = a(n) + a(n+1); the Stern-Brocot
# sequence of the task is a(1), a(2), ...
a = [0, 1]
for n in range(2, 1201):
    a.append(a[n // 2] if n % 2 == 0 else a[n // 2] + a[n // 2 + 1])
s = a[1:]
print("first 15:", *s[:15])
for v in list(range(1, 11)) + [100]:
    print(f"{v} first appears at {s.index(v) + 1}")
print("gcd of each consecutive pair of the first 1000 is 1:", "yes" if all(gcd(x, y) == 1 for x, y in zip(s[:1000], s[1:1000])) else "no")
