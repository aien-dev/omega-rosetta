# Independent reference for "Topswops" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# brute force over every deck; the reversal is a list slice, the decks come from itertools
from itertools import permutations
def swops(deck):
    deck = list(deck)
    c = 0
    while deck[0] != 1:
        m = deck[0]
        deck[:m] = deck[:m][::-1]
        c += 1
    return c
print("n  most swops")
for n in range(1, 10):
    print(f"{n}{max(swops(p) for p in permutations(range(1, n + 1))):12}")
