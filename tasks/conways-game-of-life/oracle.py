# Independent reference for "Conway's Game of Life" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# the live cells as a set of (row, col); neighbour counts come from a Counter over all live cells
from collections import Counter
def step(live, rows, cols):
    counts = Counter((r + dr, c + dc) for r, c in live
                     for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0))
    return {p for p, n in counts.items()
            if 0 <= p[0] < rows and 0 <= p[1] < cols and (n == 3 or (n == 2 and p in live))}
def run(live, rows, cols, gens):
    for g in range(gens + 1):
        print("generation", g)
        for r in range(rows):
            print("".join("#" if (r, c) in live else "." for c in range(cols)))
        live = step(live, rows, cols)
run({(1, 0), (1, 1), (1, 2)}, 3, 3, 2)
print()
run({(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}, 8, 8, 4)
