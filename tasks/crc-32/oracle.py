# Independent reference for "CRC-32" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import zlib
print(f"{zlib.crc32(b'The quick brown fox jumps over the lazy dog'):08x}")
