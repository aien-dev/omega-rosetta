# Independent reference for "100 doors" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
doors = [False] * 101
for p in range(1, 101):
    for i in range(p, 101, p):
        doors[i] = not doors[i]
print(" ".join(str(i) for i in range(1, 101) if doors[i]))
