# Independent reference for "URL decoding" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import sys, urllib.parse
for s in ["http%3A%2F%2Ffoo%20bar%2F", "google.com/search?q=%60Abdu%27l-Bah%C3%A1", "%25%32%35"]:
    sys.stdout.buffer.write(urllib.parse.unquote_to_bytes(s) + b"\n")
