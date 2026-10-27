# Independent reference for "Knight's tour" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
def onward(f, r, seen):
    return [(f + dx, r + dy) for dx, dy in moves
            if 0 <= f + dx < 8 and 0 <= r + dy < 8 and (f + dx, r + dy) not in seen]
path = [(0, 0)]
seen = {(0, 0)}
while len(path) < 64:
    cands = onward(*path[-1], seen)
    assert cands, "Warnsdorff dead end"
    nxt = min(cands, key=lambda s: len(onward(*s, seen)))   # min keeps the first of equal keys
    path.append(nxt)
    seen.add(nxt)
# the tour must be 64 distinct squares, each a knight's move from the one before
assert len(set(path)) == 64
assert all(sorted((abs(a[0] - b[0]), abs(a[1] - b[1]))) == [1, 2] for a, b in zip(path, path[1:]))
num = {s: i + 1 for i, s in enumerate(path)}
print("Warnsdorff tour from a1; each square shows its move number, rank 8 at the top")
for r in range(7, -1, -1):
    print("".join(f"{num[(f, r)]:3}" for f in range(8)))
