# Independent reference for "Letter frequency" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import collections, string
msg = "The quick brown fox jumps over the lazy dog. Pack my box with five dozen liquor jugs! Sphinx of black quartz, judge my vow."
f = collections.Counter(c for c in msg.lower() if c in string.ascii_lowercase)
for c in string.ascii_lowercase:
    print(c, f[c])
