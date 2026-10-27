# Independent reference for "Priority queue" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import heapq
tasks = ["3 Clear drains", "4 Feed cat", "5 Make tea", "1 Solve RC tasks", "2 Tax return"]
h = []
for t in tasks:
    heapq.heappush(h, (int(t.split()[0]), t))
    print("insert", t)
while h:
    print("pop", heapq.heappop(h)[1])
