# Independent reference for "Luhn test of credit card numbers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def luhn(s):
    total = 0
    for i, ch in enumerate(reversed(s)):
        d = int(ch)
        if i % 2 == 1:
            d = sum(divmod(2 * d, 10))
        total += d
    return total % 10 == 0
for s in ["49927398716", "49927398717", "1234567812345678", "1234567812345670"]:
    print(s, "valid" if luhn(s) else "invalid")
