# Independent reference for "Equilibrium index" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for a in ([-7, 1, 5, 2, -4, 3, 0], [2, 4, 6], [2, 9, 2], [1, -1, 1, -1, 1, -1, 1]):
    print(*a)
    print("equilibrium indices:" + "".join(f" {i}" for i in range(len(a)) if sum(a[:i]) == sum(a[i + 1:])))
