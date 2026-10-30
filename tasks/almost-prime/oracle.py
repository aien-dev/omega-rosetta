# Independent reference for "Almost prime" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def omega(n):
    k, p = 0, 2
    while n > 1:
        while n % p == 0:
            n //= p
            k += 1
        p += 1
    return k
for k in range(1, 6):
    out, n = [], 1
    while len(out) < 10:
        n += 1
        if omega(n) == k:
            out.append(n)
    print(f"k = {k}:" + "".join(f" {v}" for v in out))
