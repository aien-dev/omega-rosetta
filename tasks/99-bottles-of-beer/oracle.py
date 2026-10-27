# Independent reference for "99 bottles of beer" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def b(n):
    return ("No more" if n == 0 else str(n)) + (" bottle" if n == 1 else " bottles")
print("\n\n".join(f"{b(n)} of beer on the wall\n{b(n)} of beer\nTake one down, pass it around\n{b(n - 1)} of beer on the wall" for n in range(99, 0, -1)))
