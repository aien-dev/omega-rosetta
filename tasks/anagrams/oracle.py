# Independent reference for "Anagrams" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
words = ['abel', 'able', 'bale', 'bela', 'elba', 'alger', 'glare', 'lager', 'large', 'regal', 'angel', 'angle', 'galen', 'glean', 'lange', 'caret', 'carte', 'cater', 'crate', 'trace', 'evil', 'levi', 'live', 'veil', 'vile', 'elan', 'lane', 'lean', 'lena', 'neal']
groups = {}
for w in words:
    groups.setdefault("".join(sorted(w)), []).append(w)
best = max(map(len, groups.values()))
for g in groups.values():
    if len(g) == best:
        print(" ".join(g))
