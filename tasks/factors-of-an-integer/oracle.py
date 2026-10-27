# Independent reference for "Factors of an integer" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def prime_powers(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f
# every divisor is a product of prime powers p^e with 0 <= e <= the exponent of p in n
for n in [1, 45, 53, 64, 720, 1000000, 600851475143]:
    divs = [1]
    for p, e in prime_powers(n).items():
        divs = [d * p ** k for d in divs for k in range(e + 1)]
    print(f"factors of {n}: " + " ".join(map(str, sorted(divs))))
