# Independent reference for "Fusc sequence" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import functools
@functools.lru_cache(maxsize=None)
def fusc(n):
    if n < 2:
        return n
    return fusc(n // 2) if n % 2 == 0 else fusc(n // 2) + fusc(n // 2 + 1)
print("first 61 terms: " + " ".join(str(fusc(n)) for n in range(61)))
print("first term of each decimal length, below index 1000000:")
w = 0
for n in range(1000000):
    v = fusc(n)
    if len(str(v)) > w:
        w = len(str(v))
        print(f"fusc({n}) = {v}")
