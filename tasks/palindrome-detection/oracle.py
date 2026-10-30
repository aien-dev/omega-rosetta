# Independent reference for "Palindrome detection" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def exact(s):
    return s == s[::-1]
def inexact(s):
    t = "".join(c.lower() for c in s if c.isascii() and c.isalpha())
    return t == t[::-1]
yn = {True: "yes", False: "no"}
for s in ["rotor", "level", "A man, a plan, a canal: Panama!", "In girum imus nocte et consumimur igni", "hello"]:
    print(f'"{s}" exact {yn[exact(s)]} inexact {yn[inexact(s)]}')
