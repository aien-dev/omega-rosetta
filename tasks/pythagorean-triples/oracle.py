# Independent reference for "Pythagorean triples" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
# Berggren's tree of primitive triples: every primitive triple appears once, children have larger perimeters
M = [((1, -2, 2), (2, -1, 2), (2, -2, 3)), ((1, 2, 2), (2, 1, 2), (2, 2, 3)), ((-1, 2, 2), (-2, 1, 2), (-2, 2, 3))]
TOP = 10 ** 7
per = []
stack = [(3, 4, 5)]
while stack:
    t = stack.pop()
    p = sum(t)
    if p > TOP:
        continue
    per.append(p)
    for m in M:
        stack.append(tuple(sum(r[i] * t[i] for i in range(3)) for r in m))
for e in range(2, 8):
    lim = 10 ** e
    print(f"perimeter <= {lim}: {sum(lim // p for p in per if p <= lim)} triples, {sum(1 for p in per if p <= lim)} primitive")
