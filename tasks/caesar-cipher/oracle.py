# Independent reference for "Caesar cipher" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def caesar(s, k):
    out = []
    for c in s:
        if "A" <= c <= "Z":
            out.append(chr((ord(c) - 65 + k) % 26 + 65))
        elif "a" <= c <= "z":
            out.append(chr((ord(c) - 97 + k) % 26 + 97))
        else:
            out.append(c)
    return "".join(out)
e = caesar("The quick brown fox Jumped over the lazy Dog", 11)
print(e)
print(caesar(e, -11))
