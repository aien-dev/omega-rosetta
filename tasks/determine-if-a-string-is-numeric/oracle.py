# Independent reference for "Determine if a string is numeric" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
for s in ['0', '-12', '3.14', '+1e5', '1e-3', '.5', '5.', 'abc', '', '12a', '-', '1.2.3', 'e5', '1e', '--1', '6.02E+23']:
    print(f'"{s}" {"numeric" if numeric(s) else "not numeric"}')
