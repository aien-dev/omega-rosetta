# Independent reference for "Empty string" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for s in ["", "abc", ""]:
    if s == "":
        print("s is empty")
    else:
        print("s is not empty: " + s)
