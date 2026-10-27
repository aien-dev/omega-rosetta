# Independent reference for "Strip whitespace from a string/Top and tail" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
s = "  \t  hello world \t\n "
for t in (s, s.lstrip(), s.rstrip(), s.strip()):
    print("[" + t + "]")
