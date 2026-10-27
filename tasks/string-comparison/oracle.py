# Independent reference for "String comparison" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
yn = {True: "yes", False: "no"}
for a, b in [("alpha", "beta"), ("Hello", "hello"), ("abc", "abcd"), ("abcd", "abc")]:
    print(f"{a} {b} eq={yn[a == b]} lt={yn[a < b]} gt={yn[a > b]} equal-ignoring-case={yn[a.lower() == b.lower()]}")
