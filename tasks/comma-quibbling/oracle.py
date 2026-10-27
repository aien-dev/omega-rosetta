# Independent reference for "Comma quibbling" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def quibble(words):
    if len(words) <= 1:
        return "{" + "".join(words) + "}"
    return "{" + ", ".join(words[:-1]) + " and " + words[-1] + "}"
for s in ['', 'ABC', 'ABC DEF', 'ABC DEF G H']:
    print(quibble(s.split()))
