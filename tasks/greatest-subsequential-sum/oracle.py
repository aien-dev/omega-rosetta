# Independent reference for "Greatest subsequential sum" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for a in [[-1, -2, 3, 5, 6, -2, -1, 4, -4, 2, -1], [-1, -2, -3, -4], [4, -1, 2, 1, -5, 4, 0, 3], [2, -3, 2, -3, 2]]:
    print(*a)
    runs = [(sum(a[i:j]), i, j) for i in range(len(a)) for j in range(i + 1, len(a) + 1)]
    runs = [r for r in runs if r[0] > 0]
    s, i, j = min(runs, key=lambda r: (-r[0], r[1], r[2] - r[1])) if runs else (0, 0, 0)
    print("sum:", s)
    print("subsequence:" + "".join(" " + str(v) for v in a[i:j]))
