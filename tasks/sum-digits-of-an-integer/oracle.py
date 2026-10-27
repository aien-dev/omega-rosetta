# Independent reference for "Sum digits of an integer" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import string
DIG = string.digits + string.ascii_lowercase
def digits(n, b):
    out = []
    while True:
        n, r = divmod(n, b)
        out.append(r)
        if n == 0:
            return out[::-1]
for n, b in [(1, 10), (1234, 10), (0xfe, 16), (0xf0e, 16), (255, 8), (2**64 - 1, 2), (2**64 - 1, 36)]:
    ds = digits(n, b)
    print(f"{''.join(DIG[d] for d in ds)} (base {b}): digit sum {sum(ds)}")
