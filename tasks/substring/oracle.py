# Independent reference for "Substring" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
s = "abcdefgh"
n, m = 2, 3
print(s[n:n + m])
print(s[n:])
print(s[:-1])
print(s[s.index("d"):][:m])
print(s[s.index("cd"):][:m])
