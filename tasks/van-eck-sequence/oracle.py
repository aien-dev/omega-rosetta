# Independent reference for "Van Eck sequence" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
a = [0]
for n in range(999):
    prev = [m for m in range(n) if a[m] == a[n]]
    a.append(n - prev[-1] if prev else 0)
print("terms 1 to 10: " + " ".join(map(str, a[:10])))
print("terms 991 to 1000: " + " ".join(map(str, a[990:1000])))
