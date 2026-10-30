# Independent reference for "Loops/While" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
n = 1024
while n > 0:
    print(n)
    n //= 2
