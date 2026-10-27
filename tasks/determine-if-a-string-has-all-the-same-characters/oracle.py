# Independent reference for "Determine if a string has all the same characters" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for s in ["", '   ', '2', '333', '.55', 'tttTTT', '4444 444k']:
    line = f"<<<{s}>>> length {len(s)}"
    d = [i for i, c in enumerate(s) if c != s[0]]
    if d:
        print(f"{line}: first different '{s[d[0]]}' at {d[0]}")
    else:
        print(f"{line}: all the same")
