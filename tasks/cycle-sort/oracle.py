# Independent reference for "Sorting algorithms/Cycle sort" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def cycle_sort(a):
    writes = 0
    for start in range(len(a) - 1):
        item = a[start]
        pos = start + sum(1 for v in a[start + 1:] if v < item)
        if pos == start:
            continue
        while item == a[pos]:
            pos += 1
        a[pos], item = item, a[pos]
        writes += 1
        while pos != start:
            pos = start + sum(1 for v in a[start + 1:] if v < item)
            while item == a[pos]:
                pos += 1
            a[pos], item = item, a[pos]
            writes += 1
    return writes
a = [5, 0, 1, 2, 2, 3, 5, 1, 1, 0, 5, 6, 9, 8, 0, 1]
print(*a)
w = cycle_sort(a)
assert a == sorted(a)
print(*a)
print("writes:", w)
