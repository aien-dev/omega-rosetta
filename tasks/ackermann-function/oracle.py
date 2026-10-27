# Independent reference for "Ackermann function" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import sys
sys.setrecursionlimit(100000)
def A(m, n):
    return n + 1 if m == 0 else A(m - 1, 1) if n == 0 else A(m - 1, A(m, n - 1))
for m in range(4):
    for n in range(5):
        print(f"A({m}, {n}) = {A(m, n)}")
