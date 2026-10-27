# Independent reference for "Evaluate binomial coefficients" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
for n, k in [(5, 3), (10, 0), (10, 10), (33, 17), (60, 30), (67, 33)]:
    print(f"C({n}, {k}) = {math.factorial(n) // (math.factorial(k) * math.factorial(n - k))}")
