# Independent reference for "Möbius function" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def mu(n):
    f, d, m = 0, 2, n
    while d * d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0:
                return 0
            f += 1
        d += 1
    if m > 1:
        f += 1
    return -1 if f % 2 else 1
print("first 199 terms of the Moebius sequence (the first cell, n = 0, is blank):")
for r in range(10):
    print("".join("   " if n == 0 else f"{mu(n):3d}" for n in range(20 * r, 20 * r + 20)))
