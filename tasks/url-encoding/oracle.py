# Independent reference for "URL encoding" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import urllib.parse
for s in ["http://foo bar/", "mailto:joe@example.com?subject=a&b c~d_e.f-g"]:
    print("".join(c if c.isascii() and c.isalnum() else "%%%02X" % ord(c) for c in s))
    print(urllib.parse.quote(s, safe=""))
