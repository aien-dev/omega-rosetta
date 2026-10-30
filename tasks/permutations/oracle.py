# Independent reference for "Permutations" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def perms(items):
    # recursive: each element in turn first, followed by every order of the rest
    if not items:
        yield []
        return
    for i, x in enumerate(items):
        for rest in perms(items[:i] + items[i + 1:]):
            yield [x] + rest
ps = list(perms([1, 2, 3, 4]))
for p in ps:
    print(*p)
print("permutations:", len(ps))
