# Independent reference for "Recaman's sequence" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
a, seen, terms, dup = [0], {0}, [0], None
need = set(range(1, 1001))
n = 0
while need:
    n += 1
    b = a[-1] - n
    v = b if b > 0 and b not in seen else a[-1] + n
    if v in seen and dup is None:
        dup = (n, v)
    seen.add(v)
    need.discard(v)
    a.append(v)
print("first 15 terms: " + " ".join(map(str, a[:15])))
print(f"first term already seen: a({dup[0]}) = {dup[1]}")
print(f"terms a(0)..a(n) first contain every integer 0..1000 at n = {n}")
