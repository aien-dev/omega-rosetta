# Independent reference for "SHA-256" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import hashlib
for s in ["abc", "Rosetta code", "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."]:
    print(hashlib.sha256(s.encode()).hexdigest())
