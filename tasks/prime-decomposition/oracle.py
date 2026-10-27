# Independent reference for "Prime decomposition" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def f(n):
    out, d = [], 2
    while d * d <= n:
        while n % d == 0:
            out.append(d); n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out
for n in [12, 360, 97, 1001, 2147483647, 600851475143, 2**64 - 1]:
    print(f"{n} = " + " x ".join(map(str, f(n))))
