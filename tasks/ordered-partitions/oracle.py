# Independent reference for "Ordered partitions" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# Cross-check, WolframLanguageEvaluator: {4!/(2! 0! 2!), 4!/(1! 2! 1!)} -> {6, 12}
from itertools import permutations
from math import factorial
def partitions(*sizes):
    # every arrangement of 1..n cut into consecutive runs of the given sizes, keeping one per distinct
    # result; sorted by the blocks as lists gives the lexicographic order
    n = sum(sizes)
    seen = set()
    for p in permutations(range(1, n + 1)):
        blocks, k = [], 0
        for s in sizes:
            blocks.append(tuple(sorted(p[k:k + s])))
            k += s
        seen.add(tuple(blocks))
    return sorted(seen)
for sizes in ((2, 0, 2), (1, 2, 1)):
    print("partitions(" + ", ".join(map(str, sizes)) + ")")
    ps = partitions(*sizes)
    total = factorial(sum(sizes))
    for s in sizes:
        total //= factorial(s)
    assert len(ps) == total
    for blocks in ps:
        print("(" + ", ".join("{" + ", ".join(map(str, b)) + "}" for b in blocks) + ")")
