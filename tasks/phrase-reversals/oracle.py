# Independent reference for "Phrase reversals" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
s = "rosetta code phrase reversal"
print(s[::-1])
print(" ".join(w[::-1] for w in s.split(" ")))
print(" ".join(reversed(s.split(" "))))
