# Independent reference for "Sudoku" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# constraint search on candidate sets: always branch on the empty cell with the fewest candidates
puzzle = [int(c) for c in "850002400720000009004000000000107002305000900040000000000080070017000000000036040"]
def peers(c):
    r, k = divmod(c, 9)
    br, bk = r // 3 * 3, k // 3 * 3
    return {r * 9 + i for i in range(9)} | {i * 9 + k for i in range(9)} | {(br + i // 3) * 9 + bk + i % 3 for i in range(9)}
PEERS = [peers(c) - {c} for c in range(81)]
def solve(g):
    empty = [c for c in range(81) if g[c] == 0]
    if not empty:
        return g
    c = min(empty, key=lambda c: 9 - len({g[p] for p in PEERS[c]} - {0}))
    for d in sorted(set(range(1, 10)) - {g[p] for p in PEERS[c]}):
        r = solve(g[:c] + [d] + g[c + 1:])
        if r:
            return r
    return None
def show(g):
    for r in range(9):
        if r and r % 3 == 0:
            print("------+-------+------")
        print(" | ".join(" ".join(str(g[r * 9 + k]) for k in range(b, b + 3)) for b in (0, 3, 6)))
show(puzzle)
sol = solve(puzzle)
for unit in [[r * 9 + i for i in range(9)] for r in range(9)] + [[i * 9 + k for i in range(9)] for k in range(9)]:
    assert sorted(sol[c] for c in unit) == list(range(1, 10))
print("solved:")
show(sol)
