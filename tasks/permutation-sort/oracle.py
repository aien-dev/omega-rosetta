# Independent reference for "Sorting algorithms/Permutation sort" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
from itertools import permutations
a = [8, -2, 15, 3, 0, 6]
print(*a)
for tried, p in enumerate(permutations(range(len(a))), 1):
    b = [a[i] for i in p]
    if all(b[i] <= b[i + 1] for i in range(len(b) - 1)):
        break
print(*b)
print("permutations tried:", tried)
