# Independent reference for "Loops/Break" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
x = 42
def nxt():
    global x
    x = (x * 1103515245 + 12345) % 2**31
    return (x // 65536) % 20
while True:
    r = nxt()
    print(r)
    if r == 10:
        break
    print(nxt())
