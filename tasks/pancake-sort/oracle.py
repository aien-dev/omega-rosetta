# Independent reference for "Sorting algorithms/Pancake sort" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
a = [23, -7, 61, 4, 0, 38, 15, -7, 90, 2, 11]
print(*a)
flips = 0
for size in range(len(a), 1, -1):
    m = max(range(size), key=lambda i: (a[i], -i))
    if m != size - 1:
        if m != 0:
            a[:m + 1] = a[:m + 1][::-1]
            flips += 1
        a[:size] = a[:size][::-1]
        flips += 1
assert a == sorted(a)
print(*a)
print("flips:", flips)
