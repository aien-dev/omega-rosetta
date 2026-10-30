# Independent reference for "Sorting algorithms/Bogosort" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
M = 2 ** 64
x = 0
def rnd():
    global x
    x = (x * 6364136223846793005 + 1442695040888963407) % M
    return x >> 33
a = [3, -1, 4, 1, 5, 9, 2]
print(*a)
c = 0
while a != sorted(a):
    for i in range(len(a) - 1, 0, -1):
        j = rnd() % (i + 1)
        a[i], a[j] = a[j], a[i]
    c += 1
print(*a)
print("shuffles:", c)
