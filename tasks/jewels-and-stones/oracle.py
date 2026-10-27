# Independent reference for "Jewels and stones" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for s, j in [("aAAbbbb", "aA"), ("ZZ", "z")]:
    print(s, j, sum(c in j for c in s))
