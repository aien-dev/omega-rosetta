# Independent reference for "Mandelbrot set" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
pal = " .:-=+*%"
for r in range(24):
    ci = 1.15 - float(r) * 0.1
    line = ""
    for c in range(72):
        cr = float(c) * 0.0375 - 2.2
        zr = zi = 0.0
        it = 0
        while it < 50:
            zr2 = zr * zr
            zi2 = zi * zi
            if zr2 + zi2 > 4.0:
                break
            zi = 2.0 * zr * zi + ci
            zr = zr2 - zi2 + cr
            it += 1
        line += "#" if it == 50 else pal[it % 8]
    print(line)
