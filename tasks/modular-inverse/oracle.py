# Independent reference for "Modular inverse" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for a, m in [(42, 2017), (40, 1), (52, 217), (-486, 217), (40, 2018), (1234567, 1000000007)]:
    try:
        print(f"{a}^-1 mod {m} = {pow(a, -1, m)}")
    except ValueError:
        print(f"{a}^-1 mod {m} does not exist")
