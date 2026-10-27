# Independent reference for "Digital root" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for n in [627615, 39390, 588225, 393900588225, 0, 9, 199, 18446744073709551615]:
    v, p = n, 0
    while v > 9:
        v = sum(map(int, str(v)))
        p += 1
    print(f"{n}: additive persistence {p}, digital root {v}")
