# Independent reference for "SHA-1" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import hashlib
for s in ["", 'abc', 'Rosetta Code', 'The quick brown fox jumps over the lazy dog', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']:
    print(hashlib.sha1(s.encode()).hexdigest())
