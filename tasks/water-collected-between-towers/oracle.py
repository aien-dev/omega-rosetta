# Independent reference for "Water collected between towers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for towers in [[1, 5, 3, 7, 2], [5, 3, 7, 2, 6, 4, 5, 9, 1, 2], [2, 6, 3, 5, 2, 8, 1, 4, 2, 2, 5, 3, 5, 7, 4, 1], [5, 5, 5, 5], [5, 6, 7, 8], [8, 7, 7, 6], [6, 7, 10, 7, 6]]:
    print(*towers)
    # fill level by level: at height h, count the empty cells strictly between the outermost towers >= h
    water = 0
    for h in range(1, max(towers) + 1):
        idx = [i for i, t in enumerate(towers) if t >= h]
        water += sum(1 for i in range(idx[0], idx[-1] + 1) if towers[i] < h)
    print("water:", water)
