# Independent reference for "Greatest common divisor" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
for a, b in [(1071, 1029), (40902, 24140), (12, 18), (17, 5), (0, 5), (2**64 - 1, 6148914691236517205)]:
    print(f"gcd({a}, {b}) = {math.gcd(a, b)}")
