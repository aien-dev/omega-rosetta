# Independent reference for "ISBN13 check digit" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def ok(s):
    d = [int(c) for c in s if c.isdigit()]
    return len(d) == 13 and sum(x * (3 if i % 2 else 1) for i, x in enumerate(d)) % 10 == 0
for s in ["978-0596528126", "978-0596528120", "978-1788399081", "978-1788399083"]:
    print(f"{s}: {'good' if ok(s) else 'bad'}")
