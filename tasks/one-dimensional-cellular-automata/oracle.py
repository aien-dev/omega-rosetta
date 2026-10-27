# Independent reference for "One-dimensional cellular automata" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
cells = "_###_##_#_#_#_#__#__"
g = 0
while True:
    print(f"generation {g}: {cells}")
    padded = "_" + cells + "_"
    nxt = "".join("#" if padded[i - 1:i + 2].count("#") == 2 else "_" for i in range(1, len(cells) + 1))
    if nxt == cells:
        break
    cells, g = nxt, g + 1
