# Independent reference for "Cuban primes" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True
cub, n = [], 0
while len(cub) < 100000:
    n += 1
    v = (n + 1) ** 3 - n ** 3
    if is_prime(v):
        cub.append(v)
print("first 200 cuban primes:")
for i in range(0, 200, 10):
    print(" ".join(map(str, cub[i:i + 10])))
print(f"the 100000th cuban prime: {cub[-1]}")
