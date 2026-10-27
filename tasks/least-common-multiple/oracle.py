# Independent reference for "Least common multiple" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import functools, math
for a, b in [(12, 18), (35, 0), (0, 5), (4294967296, 6000000000)]:
    print(f"lcm({a}, {b}) = {math.lcm(a, b)}")
for n in [10, 20, 40]:
    print(f"lcm(1..{n}) = {functools.reduce(math.lcm, range(1, n + 1))}")
