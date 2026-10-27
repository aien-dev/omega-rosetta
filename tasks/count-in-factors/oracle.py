# Independent reference for "Count in factors" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def factors(n):
    out, p = [], 2
    while p * p <= n:
        while n % p == 0:
            out.append(p)
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out.append(n)
    return out
for n in list(range(1, 26)) + list(range(2144, 2157)) + [600851475143, 1000000000000]:
    print(f"{n} = " + (" x ".join(map(str, factors(n))) if n > 1 else "1"))
