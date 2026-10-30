# Independent reference for "Isqrt (integer square root) of X" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
print("isqrt of 0..65: " + " ".join(str(math.isqrt(x)) for x in range(66)))
for n in range(1, 22, 2):
    print(f"isqrt(7^{n}) = {math.isqrt(7 ** n)}")
