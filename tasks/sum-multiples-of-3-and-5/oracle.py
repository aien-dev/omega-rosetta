# Independent reference for "Sum multiples of 3 and 5" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
print(f"by loop, below 1000: {sum(set(range(0, 1000, 3)) | set(range(0, 1000, 5)))}")
for e in range(1, 10):
    n = 10 ** e
    print(f"by formula, below 10^{e}: {sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0) if e <= 6 else (sum(range(0, n, 3)) + sum(range(0, n, 5)) - sum(range(0, n, 15)))}")
