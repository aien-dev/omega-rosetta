# Independent reference for "Roman numerals/Encode" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def roman(n):
    out = ""
    for v, s in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
                 (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
        while n >= v:
            out += s; n -= v
    return out
for n in [1990, 2008, 1666, 3999, 4, 14, 1]:
    print(f"{n} = {roman(n)}")
