# Independent reference for "Happy numbers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(c) ** 2 for c in str(n))
    return n == 1
hs = [n for n in range(1, 100) if happy(n)][:8]
print("first 8 happy numbers: " + " ".join(map(str, hs)))
