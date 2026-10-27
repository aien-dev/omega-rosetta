# Independent reference for "N-queens problem" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
from itertools import permutations
for n in range(1, 9):
    c = sum(1 for p in permutations(range(n))
            if len({p[i] + i for i in range(n)}) == n and len({p[i] - i for i in range(n)}) == n)
    print(f"{n} queens: {c} solutions")
