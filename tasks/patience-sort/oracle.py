# Independent reference for "Sorting algorithms/Patience sort" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import heapq
a = [4, 65, 2, -31, 0, 99, 83, 782, 1, 4, -31, 18]
print(*a)
piles = []
for v in a:
    for p in piles:
        if p[-1] >= v:
            p.append(v)
            break
    else:
        piles.append([v])
heap = [(p[-1], i) for i, p in enumerate(piles)]
heapq.heapify(heap)
out = []
while heap:
    v, i = heapq.heappop(heap)
    out.append(piles[i].pop())
    if piles[i]:
        heapq.heappush(heap, (piles[i][-1], i))
assert out == sorted(a)
print(*out)
