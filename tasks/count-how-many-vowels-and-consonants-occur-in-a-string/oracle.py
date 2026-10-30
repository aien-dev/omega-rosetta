# Independent reference for "Count how many vowels and consonants occur in a string" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
s = "Now is the time for all good men to come to the aid of their country.".lower()
letters = [c for c in s if "a" <= c <= "z"]
v = [c for c in letters if c in "aeiou"]
c = [c for c in letters if c not in "aeiou"]
print(f"vowels {len(v)}, consonants {len(c)}")
print(f"distinct vowels {len(set(v))}, consonants {len(set(c))}")
