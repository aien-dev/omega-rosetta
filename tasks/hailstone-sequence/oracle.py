# Independent reference for "Hailstone sequence" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def h(n):
    s = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        s.append(n)
    return s
s = h(27)
print(f"hailstone(27) has {len(s)} elements: {' '.join(map(str, s[:4]))} ... {' '.join(map(str, s[-4:]))}")
n = max(range(1, 100000), key=lambda n: len(h(n)))
print(f"below 100000 the longest is {n} with {len(h(n))} elements")
