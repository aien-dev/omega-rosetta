# Independent reference for "Twin primes" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import bisect, itertools
N = 10**8
s = bytearray([1]) * N
s[0] = s[1] = 0
for i in range(2, 10**4):
    if s[i]:
        s[i * i::i] = bytes(len(range(i * i, N, i)))
ps = list(itertools.compress(range(N), s))
# the larger member of each twin pair, so "below lim" means that member < lim
big = [p + 2 for p in ps if p + 2 < N and s[p + 2]]
for e in range(1, 9):
    print(f"twin prime pairs below {10**e}: {bisect.bisect_left(big, 10**e)}")
