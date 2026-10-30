# Independent reference for "Smith numbers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
ds = lambda n: sum(map(int, str(n)))
def factor(n):
    f, p = [], 2
    while p * p <= n:
        while n % p == 0:
            f.append(p)
            n //= p
        p += 1
    return f + ([n] if n > 1 else [])
sm = [n for n in range(2, 10000) if len(factor(n)) > 1 and ds(n) == sum(ds(p) for p in factor(n))]
print(f"Smith numbers below 10000: {len(sm)}")
print("first 20: " + " ".join(map(str, sm[:20])))
print("last 10: " + " ".join(map(str, sm[-10:])))
