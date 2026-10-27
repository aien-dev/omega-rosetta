# Independent reference for "Catalan numbers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
print("n, C(n) by C(n+1) = 2(2n+1)/(n+2) C(n), and again by C(n+1) = sum C(i) C(n-i):")
for n in range(15):
    c = math.comb(2 * n, n) // (n + 1)
    print(f"C({n}) = {c} by the recurrence, {c} by the convolution sum")
