# Independent reference for "Wireworld" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
rows = ["tH.........", ".   .      ", "   ...     ", ".   .      ", "Ht.. ......"]
def step(g):
    def heads(r, c):
        return sum(1 for dr in (-1, 0, 1) for dc in (-1, 0, 1)
                   if (dr or dc) and 0 <= r + dr < len(g) and 0 <= c + dc < len(g[0]) and g[r + dr][c + dc] == "H")
    nxt = {"H": "t", "t": ".", " ": " "}
    return ["".join(nxt.get(ch) or ("H" if heads(r, c) in (1, 2) else ".") for c, ch in enumerate(row))
            for r, row in enumerate(g)]
for gen in range(10):
    print("generation", gen)
    print("\n".join(rows))
    rows = step(rows)
