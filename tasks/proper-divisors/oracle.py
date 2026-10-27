# Independent reference for "Proper divisors" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
def proper(n):
    small = [d for d in range(1, math.isqrt(n) + 1) if n % d == 0]
    return sorted((set(small) | {n // d for d in small}) - {n})
for n in range(1, 11):
    print(f"{n}:" + "".join(f" {d}" for d in proper(n)))
best = max(range(1, 20001), key=lambda n: (len(proper(n)), -n))
print(f"the number in 1..20000 with the most proper divisors: {best} has {len(proper(best))} proper divisors")
