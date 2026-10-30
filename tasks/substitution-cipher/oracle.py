# Independent reference for "Substitution cipher" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import string
key = "phqgiumeaylnofdxjkrcvstzwb"
msg = "the quick brown fox jumps over the lazy dog, 42 times"
enc = str.maketrans(string.ascii_lowercase, key)
dec = str.maketrans(key, string.ascii_lowercase)
e = msg.translate(enc)
print(msg)
print(e)
print(e.translate(dec))
