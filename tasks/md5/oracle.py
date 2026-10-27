# Independent reference for "MD5" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import hashlib
for s in ["", 'The quick brown fox jumps over the lazy dog', "The quick brown fox jumped over the lazy dog's back", 'Rosetta Code', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']:
    print(hashlib.md5(s.encode()).hexdigest())
