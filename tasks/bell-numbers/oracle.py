# Independent reference for "Bell numbers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
# Bell numbers by B(n+1) = sum C(n, k) B(k); the triangle rows by the Aitken array rule
B = [1]
for n in range(60):
    B.append(sum(math.comb(n, k) * B[k] for k in range(n + 1)))
print("first 10 rows of the Bell triangle:")
r = [1]
for i in range(10):
    print(" ".join(map(str, r)))
    nr = [r[-1]]
    for v in r:
        nr.append(nr[-1] + v)
    r = nr
print("first 15 Bell numbers: " + " ".join(map(str, B[:15])))
print(f"B(49), the 50th Bell number: {B[49]}")
