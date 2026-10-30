# Independent reference for "Gray code" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# reflected construction: the n-bit code is 0 + the (n-1)-bit code, then 1 + that code reversed
codes = [""]
for _ in range(5):
    codes = ["0" + c for c in codes] + ["1" + c for c in reversed(codes)]
print("number  binary  gray   decoded")
for n, g in enumerate(codes):
    print(f"{n:6}  {n:05b}   {g}  {codes.index(g):7}")
