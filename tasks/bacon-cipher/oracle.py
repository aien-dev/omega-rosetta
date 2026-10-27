# Independent reference for "Bacon cipher" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
secret = "rosetta code"
cover = "bacon's cipher is a method of steganography devised by francis bacon. a message is concealed in the presentation of text rather than its content."
bits = "".join(format(26 if c == " " else ord(c) - 97, "05b") for c in secret)
out, b = [], 0
for c in cover:
    if "a" <= c <= "z" and b < len(bits):
        if bits[b] == "1":
            c = c.upper()
        b += 1
    out.append(c)
enc = "".join(out)
print(enc)
got = "".join("1" if c.isupper() else "0" for c in enc if c.isalpha())[:len(bits)]
print("".join(" " if int(got[i:i + 5], 2) == 26 else chr(97 + int(got[i:i + 5], 2)) for i in range(0, len(got), 5)))
