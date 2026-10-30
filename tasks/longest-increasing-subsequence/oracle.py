# Independent reference for "Longest increasing subsequence" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
from itertools import combinations
for a in ([3, 2, 6, 4, 5, 1], [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]):
    print(*a)
    best = []
    for k in range(len(a), 0, -1):
        found = [[a[i] for i in c] for c in combinations(range(len(a)), k)
                 if all(a[c[t]] < a[c[t + 1]] for t in range(k - 1))]
        if found:
            best = min(found)
            break
    print(*best)
