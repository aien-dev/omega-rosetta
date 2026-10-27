# Independent reference for "Kaprekar numbers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def kaprekar(n):
    if n == 1:
        return True
    s = str(n * n)
    for i in range(1, len(s)):
        a, b = int(s[:i]), int(s[i:])
        if b > 0 and a + b == n:
            return True
    return False
ks = [n for n in range(1, 10**6) if kaprekar(n)]
print("Kaprekar numbers below 10000: " + " ".join(str(k) for k in ks if k < 10000))
print(f"count of Kaprekar numbers below 1000000: {len(ks)}")
