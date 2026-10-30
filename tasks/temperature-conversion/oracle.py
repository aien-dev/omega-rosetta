# Independent reference for "Temperature conversion" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
from fractions import Fraction as F
def fmt(x):
    c = round(x * 100)
    assert c == x * 100
    return ("-" if c < 0 else "") + f"{abs(c) // 100}.{abs(c) % 100:02d}"
for k100 in [2100, 0, 27315, 37315, 31015]:
    k = F(k100, 100)
    print("K ", fmt(k))
    print("C ", fmt(k - F(27315, 100)))
    print("F ", fmt(k * F(9, 5) - F(45967, 100)))
    print("R ", fmt(k * F(9, 5)))
    print()
