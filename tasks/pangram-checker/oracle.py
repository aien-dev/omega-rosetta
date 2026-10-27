# Independent reference for "Pangram checker" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import string
for s in ["The quick brown fox jumps over the lazy dog", "The quick brown fox jumped over the lazy dog", "Pack my box with five dozen liquor jugs."]:
    ok = set(string.ascii_lowercase) <= set(s.lower())
    print(f'"{s}" is {"a" if ok else "not a"} pangram')
