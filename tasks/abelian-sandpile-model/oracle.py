# Independent reference for "Abelian sandpile model" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# a work list of full cells, each toppling all its whole fours at once
def pile(n, grains):
    g = {(r, c): 0 for r in range(n) for c in range(n)}
    g[n // 2, n // 2] = grains
    work, tops = [(n // 2, n // 2)], 0
    while work:
        r, c = work.pop()
        k = g[r, c] // 4
        if k == 0:
            continue
        g[r, c] -= 4 * k
        tops += k
        for p in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if p in g:
                g[p] += k
                if g[p] >= 4:
                    work.append(p)
    for r in range(n):
        print(" ".join(str(g[r, c]) for c in range(n)))
    print("topplings:", tops)
for t, (n, grains) in enumerate(((5, 16), (7, 64), (9, 200))):
    if t:
        print()
    pile(n, grains)
