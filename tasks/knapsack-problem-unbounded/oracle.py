# Independent reference for "Knapsack problem/Unbounded" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
from fractions import Fraction as F
from itertools import product
items = [("panacea", 3000, F("0.3"), F("0.025")), ("ichor", 1800, F("0.2"), F("0.015")), ("gold", 2500, F("2.0"), F("0.002"))]
W, V = F(25), F("0.25")
fits = []
for n in product(*(range(int(min(W / w, V / v)) + 1) for _, _, w, v in items)):
    w = sum(k * it[2] for k, it in zip(n, items))
    v = sum(k * it[3] for k, it in zip(n, items))
    if w <= W and v <= V:
        fits.append((sum(k * it[1] for k, it in zip(n, items)), n, w, v))
best = max(f[0] for f in fits)
print("panacea ichor gold value weight volume")
for val, n, w, v in sorted(f for f in fits if f[0] == best):
    print(*n, val, f"{int(w * 10)}/10", f"{int(v * 1000)}/1000")
