# Independent reference for "String matching" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
s, t = "tacoloco", "co"
yn = {True: "yes", False: "no"}
print("starts with:", yn[s.startswith(t)])
print("found at:" + "".join(f" {i}" for i in range(len(s)) if s.startswith(t, i)))
print("ends with:", yn[s.endswith(t)])
