# Independent reference for "Remove vowels from a string" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
s = "Rosetta Code is a programming chrestomathy site, AEIOU and aeiou alike."
print(s)
print("".join(c for c in s if c not in "aeiouAEIOU"))
