# Independent reference for "Loops/Do-while" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
v = 0
while True:
    v += 1
    print(v)
    if v % 6 == 0:
        break
