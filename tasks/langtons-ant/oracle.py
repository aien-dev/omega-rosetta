# Independent reference for "Langton's ant" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# the black cells as a set; the heading as a complex number (up = -1j with rows growing downward)
black = set()
pos, head = complex(50, 50), -1j   # real part = column, imaginary part = row
steps = 0
while 0 <= pos.real < 100 and 0 <= pos.imag < 100:
    if pos in black:
        head *= -1j      # left turn
        black.remove(pos)
    else:
        head *= 1j       # right turn
        black.add(pos)
    pos += head
    steps += 1
print("steps until the ant leaves the grid:", steps)
rows = [int(p.imag) for p in black]
cols = [int(p.real) for p in black]
print(f"black cells, rows and columns {min(rows)}..{max(rows)} {min(cols)}..{max(cols)}")
for r in range(min(rows), max(rows) + 1):
    print("".join("#" if complex(c, r) in black else "." for c in range(min(cols), max(cols) + 1)))
