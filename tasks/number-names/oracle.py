# Independent reference for "Number names" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
SCALES = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]
def below_1000(n):
    parts = []
    if n >= 100:
        parts.append(ONES[n // 100] + " hundred")
    r = n % 100
    if 0 < r < 20:
        parts.append(ONES[r])
    elif r >= 20:
        parts.append(TENS[r // 10 - 2] + ("-" + ONES[r % 10] if r % 10 else ""))
    return " ".join(parts)
def spell(n):
    if n == 0:
        return "zero"
    groups = []
    i = 0
    while n:
        n, g = divmod(n, 1000)
        if g:
            groups.append(below_1000(g) + (" " + SCALES[i] if i else ""))
        i += 1
    return " ".join(reversed(groups))
for n in [0, 7, 13, 21, 99, 100, 101, 999, 1000, 1001, 12345, 1000000, 1234567890, 18446744073709551615]:
    print(f"{n}: {spell(n)}")
