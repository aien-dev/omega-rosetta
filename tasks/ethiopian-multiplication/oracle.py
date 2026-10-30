# Independent reference for "Ethiopian multiplication" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
a, b, s = 17, 34, 0
l, r = a, b
while l >= 1:
    print(l, r, "STRUCK" if l % 2 == 0 else "KEPT")
    if l % 2:
        s += r
    l, r = l // 2, r * 2
assert s == a * b
print(f"{a} x {b} = {s}")
