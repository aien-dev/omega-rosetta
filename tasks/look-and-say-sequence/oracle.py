# Independent reference for "Look-and-say sequence" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import itertools
s = "1"
for _ in range(15):
    print(s)
    s = "".join(str(len(list(g))) + k for k, g in itertools.groupby(s))
