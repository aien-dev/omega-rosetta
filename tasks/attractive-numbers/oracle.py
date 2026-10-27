# Independent reference for "Attractive numbers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def omega(n):
    k, p = 0, 2
    while n > 1:
        while n % p == 0:
            n //= p
            k += 1
        p += 1
    return k
att = [n for n in range(1, 121) if omega(n) in (2, 3, 5, 7)]
print("attractive numbers up to 120 (the count of prime factors, with multiplicity, is prime):")
for i in range(0, len(att), 20):
    print("".join(f"{n:4d}" for n in att[i:i + 20]))
