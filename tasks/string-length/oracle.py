# Independent reference for "String length" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import sys
out = sys.stdout.buffer
for s in ["møøse", "𝔘𝔫𝔦𝔠𝔬𝔡𝔢", "J̲o̲s̲é̲"]:
    out.write(f"{s}\n{len(s.encode('utf-8'))} bytes {len(s)} characters\n".encode("utf-8"))
