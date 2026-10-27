# Independent reference for "Ordered words" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
words = ['almost', 'abbey', 'accent', 'begin', 'biopsy', 'chimp', 'chintz', 'deist', 'effort', 'first', 'ghost', 'glory', 'floor', 'knotty', 'billowy', 'bijoux', 'abhors', 'aegilops', 'this', 'that', 'zebra', 'bellow', 'adder', 'cello']
ordered = [w for w in words if list(w) == sorted(w)]
best = max(map(len, ordered))
for w in ordered:
    if len(w) == best:
        print(w)
