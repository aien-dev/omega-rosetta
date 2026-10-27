# Independent reference for "Rot-13" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import codecs
for s in ["Hello, World!", "The Quick Brown Fox Jumps Over The Lazy Dog."]:
    print(codecs.encode(s, "rot13"))
