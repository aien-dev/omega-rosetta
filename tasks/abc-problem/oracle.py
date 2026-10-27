# Independent reference for "ABC problem" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
blocks = "BO XK DQ CP NA GT RE TG QD FS JW HU VI AN OB ER FS LY PC ZM".split()
def can(word, used):
    if not word:
        return True
    for i, b in enumerate(blocks):
        if i not in used and word[0] in b and can(word[1:], used | {i}):
            return True
    return False
for w in ['A', 'BARK', 'BOOK', 'TREAT', 'COMMON', 'SQUAD', 'CONFUSE']:
    print(w, "yes" if can(w, frozenset()) else "no")
