# Independent reference for "Determine if a string has all unique characters" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for s in ["", '.', 'abcABC', 'XYZ ZYX', '1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ']:
    line = f"<<<{s}>>> length {len(s)}"
    for i, c in enumerate(s):
        j = s.find(c, i + 1)
        if j >= 0:
            print(f"{line}: duplicate '{c}' at {i} and {j}")
            break
    else:
        print(f"{line}: all unique")
