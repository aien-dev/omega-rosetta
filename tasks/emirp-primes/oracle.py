# Independent reference for "Emirp primes" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
N = 10**6
s = bytearray([1]) * N
s[0] = s[1] = 0
for i in range(2, 1000):
    if s[i]:
        s[i * i::i] = bytes(len(range(i * i, N, i)))
def emirp(n):
    r = int(str(n)[::-1])
    return s[n] and r != n and s[r]
em = [n for n in range(N) if emirp(n)]
print("first 20 emirps: " + " ".join(map(str, em[:20])))
print("emirps between 7700 and 8000: " + " ".join(str(n) for n in em if 7700 <= n <= 8000))
print(f"the 10000th emirp: {em[9999]}")
