# Independent reference for "Combinations" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# recursive: either take the smallest remaining element or skip it
def combs(start, n, k):
    if k == 0:
        yield []
        return
    for i in range(start, n - k + 1):
        for rest in combs(i + 1, n, k - 1):
            yield [i] + rest
cs = list(combs(0, 5, 3))
for c in cs:
    print(*c)
print("combinations:", len(cs))
