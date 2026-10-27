# Independent reference for "Thue-Morse" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for k in range(7):
    print("".join(str(bin(i).count("1") % 2) for i in range(2 ** k)))
