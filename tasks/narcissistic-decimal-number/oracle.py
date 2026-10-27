# Independent reference for "Narcissistic decimal number" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# by digit multisets: for each length k and each sorted choice of k digits, the power sum is
# narcissistic when its own digits, sorted, are that choice
import itertools
found = set()
for k in range(1, 8):
    for combo in itertools.combinations_with_replacement(range(10), k):
        s = sum(d ** k for d in combo)
        if len(str(s)) == k and tuple(sorted(map(int, str(s)))) == combo:
            found.add(s)
found.add(0)
print("first 25 narcissistic decimal numbers: " + " ".join(map(str, sorted(found)[:25])))
