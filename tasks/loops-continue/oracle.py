# Independent reference for "Loops/Continue" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for i in range(1, 11):
    print(i, end="")
    if i % 5 == 0:
        print()
        continue
    print(", ", end="")
