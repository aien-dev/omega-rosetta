# Independent reference for "Binary search" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import bisect
a = [-40, -12, -3, 0, 2, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
for x in [-40, 0, 21, 610, 7, 1000, -41]:
    i = bisect.bisect_left(a, x)
    print(f"{x} found at index {i}" if i < len(a) and a[i] == x else f"{x} not found")
