# Independent reference for "Run-length encoding" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import itertools, re
msg = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
e = "".join(f"{len(list(g))}{c}" for c, g in itertools.groupby(msg))
print(e)
print("".join(c * int(n) for n, c in re.findall(r"(\d+)(\D)", e)))
