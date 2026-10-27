# Independent reference for "Floyd's triangle" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for t, n in enumerate((5, 14)):
    if t:
        print()
    rows, k = [], 1
    for r in range(n):
        rows.append(list(range(k, k + r + 1)))
        k += r + 1
    widths = [len(str(v)) for v in rows[-1]]
    for row in rows:
        print(" ".join(str(v).rjust(w) for v, w in zip(row, widths)))
