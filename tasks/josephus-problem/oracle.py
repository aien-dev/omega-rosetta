# Independent reference for "Josephus problem" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# the survivor by the recurrence J(1) = 0, J(m) = (J(m-1) + k) mod m, the order by rotating a list
n, k = 41, 3
j = 0
for m in range(2, n + 1):
    j = (j + k) % m
ring = list(range(n))
order = []
pos = 0
while len(ring) > 1:
    pos = (pos + k - 1) % len(ring)
    order.append(ring.pop(pos))
assert ring == [j]
print("executed in order:", *order)
print("survivor:", j)
