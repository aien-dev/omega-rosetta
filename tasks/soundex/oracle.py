# Independent reference for "Soundex" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
groups = {"bfpv": "1", "cgjkqsxz": "2", "dt": "3", "l": "4", "mn": "5", "r": "6", "hw": "h"}
def code(c):
    for k, v in groups.items():
        if c in k:
            return v
    return "0"
def soundex(name):
    s = name.lower()
    out = s[0].upper()
    prev = code(s[0])
    for c in s[1:]:
        d = code(c)
        if d == "h":
            continue
        if d == "0":
            prev = d
            continue
        if d != prev:
            out += d
        prev = d
    return (out + "000")[:4]
for name in ['Robert', 'Rupert', 'Rubin', 'Ashcraft', 'Ashcroft', 'Tymczak', 'Pfister', 'Honeyman', 'Lee', 'Gutierrez', 'Jackson', 'VanDeusen']:
    print(name, soundex(name))
