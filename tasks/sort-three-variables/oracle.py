# Independent reference for "Sort three variables" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for vals in ([77444, -12, 0], ['lions, tigers, and', 'bears, oh my!', '(from the "Wizard of OZ")']):
    for x in (vals, sorted(vals, key=lambda s: s.encode() if isinstance(s, str) else s)):
        for name, v in zip("xyz", x):
            print(f"{name} = {v}")
