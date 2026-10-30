# Independent reference for "Strip a set of characters from a string" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
s = "She was a soul stripper. She took my heart!"
print("".join(c for c in s if c not in "aei"))
