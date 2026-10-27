# Independent reference for "Ludic numbers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
lst = list(range(2, 22000))
lud = [1]
while lst:
    lud.append(lst[0])
    del lst[::lst[0]]
s = set(lud)
print("first 25 ludic numbers: " + " ".join(map(str, lud[:25])))
print(f"ludic numbers <= 1000: {sum(1 for x in lud if x <= 1000)}")
print("2000th to 2005th ludic numbers: " + " ".join(map(str, lud[1999:2005])))
print("ludic triplets (x, x+2, x+6) below 250: " +
      " ".join(f"({x}, {x + 2}, {x + 6})" for x in lud if x + 6 < 250 and x + 2 in s and x + 6 in s))
