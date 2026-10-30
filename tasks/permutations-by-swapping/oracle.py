# Independent reference for "Permutations by swapping" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# the same order built recursively: the element n sweeps right to left through the first order of
# n-1 elements, then left to right through the next, and so on; the sign is the inversion parity
def sjt(n):
    if n == 1:
        return [[1]]
    out = []
    for i, p in enumerate(sjt(n - 1)):
        spots = range(n - 1, -1, -1) if i % 2 == 0 else range(n)
        out += [p[:k] + [n] + p[k:] for k in spots]
    return out
def sign(p):
    inv = sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j])
    return -1 if inv % 2 else 1
for n in (3, 4):
    if n == 4:
        print()
    for p in sjt(n):
        print(f"Perm: [{', '.join(map(str, p))}] Sign: {sign(p)}")
