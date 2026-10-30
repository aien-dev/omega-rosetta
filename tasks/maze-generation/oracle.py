# Independent reference for "Maze generation" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
M = 2 ** 64
x = 0
def rnd():
    global x
    x = (x * 6364136223846793005 + 1442695040888963407) % M
    return x >> 33
W, H = 10, 6
def generate():
    east = [[True] * W for _ in range(H)]
    south = [[True] * W for _ in range(H)]
    seen = {(0, 0)}
    stack = [(0, 0)]
    while stack:
        r, k = stack[-1]
        cands = [(r + dr, k + dk) for dr, dk in ((-1, 0), (0, 1), (1, 0), (0, -1))
                 if 0 <= r + dr < H and 0 <= k + dk < W and (r + dr, k + dk) not in seen]
        if not cands:
            stack.pop()
            continue
        nr, nk = cands[rnd() % len(cands)]
        if nr == r:
            east[r][min(k, nk)] = False
        else:
            south[min(r, nr)][k] = False
        seen.add((nr, nk))
        stack.append((nr, nk))
    return east, south
def draw(east, south, marked=()):
    print("+" + "---+" * W)
    for r in range(H):
        print("|" + "".join((" * " if (r, k) in marked else "   ") + ("|" if east[r][k] else " ") for k in range(W)))
        print("+" + "".join("---+" if south[r][k] else "   +" for k in range(W)))
east, south = generate()
# a perfect maze: 60 cells joined by exactly 59 openings, all reachable from the top-left cell
openings = sum(not e for row in east for e in row[:W - 1]) + sum(not s for row in south[:H - 1] for s in row)
assert openings == W * H - 1
draw(east, south)
