# Independent reference for "Knapsack problem/0-1" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
from itertools import combinations
items = [('map', 9, 150), ('compass', 13, 35), ('water', 153, 200), ('sandwich', 50, 160), ('glucose', 15, 60), ('tin', 68, 45), ('banana', 27, 60), ('apple', 39, 40), ('cheese', 23, 30), ('beer', 52, 10), ('suntan cream', 11, 70), ('camera', 32, 30), ('T-shirt', 24, 15), ('trousers', 48, 10), ('umbrella', 73, 40), ('waterproof trousers', 42, 70), ('waterproof overclothes', 43, 75), ('note-case', 22, 80), ('sunglasses', 7, 20), ('towel', 18, 12), ('socks', 4, 50), ('book', 30, 10)]
# exhaustive search is 2^22 subsets; branch and bound over items sorted by value density keeps it quick
order = sorted(range(len(items)), key=lambda i: -items[i][2] / items[i][1])
best = (0, ())
def bound(k, w, v):
    for i in order[k:]:
        if w + items[i][1] <= 400:
            w += items[i][1]; v += items[i][2]
        else:
            return v + (400 - w) * items[i][2] / items[i][1]
    return v
def go(k, w, v, chosen):
    global best
    if v > best[0]:
        best = (v, chosen)
    if k == len(order) or bound(k, w, v) <= best[0]:
        return
    i = order[k]
    if w + items[i][1] <= 400:
        go(k + 1, w + items[i][1], v + items[i][2], chosen + (i,))
    go(k + 1, w, v, chosen)
go(0, 0, 0, ())
for i in sorted(best[1]):
    print(items[i][0])
print("total weight", sum(items[i][1] for i in best[1]))
print("total value", best[0])
