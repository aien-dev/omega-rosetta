# Independent reference for "Vigenère cipher" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
key = "VIGENERECIPHER"
msg = "Beware the Jabberwock, my son! The jaws that bite, the claws that catch!"
t = "".join(c.upper() for c in msg if c.isalpha())
e = "".join(chr((ord(c) - 65 + ord(key[i % len(key)]) - 65) % 26 + 65) for i, c in enumerate(t))
d = "".join(chr((ord(c) - 65 - (ord(key[i % len(key)]) - 65)) % 26 + 65) for i, c in enumerate(e))
print(t)
print(e)
print(d)
