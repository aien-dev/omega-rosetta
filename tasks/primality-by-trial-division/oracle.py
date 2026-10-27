# Independent reference for "Primality by trial division" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))
print("primes below 100: " + " ".join(str(n) for n in range(100) if prime(n)))
for n in [1, 2, 9, 561, 7919, 2147483647, 999999999989, 999999999999, 1000000000039]:
    print(f"{n} is {'prime' if prime(n) else 'not prime'}")
