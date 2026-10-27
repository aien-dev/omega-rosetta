# Independent reference for "Perfect totient numbers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def phi(n):
    r, m, p = n, n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r
out, n = [], 1
while len(out) < 20:
    n += 1
    s, v = 0, n
    while v != 1:
        v = phi(v)
        s += v
    if s == n:
        out.append(n)
print("first 20 perfect totient numbers: " + " ".join(map(str, out)))
