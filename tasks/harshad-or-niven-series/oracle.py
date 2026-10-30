# Independent reference for "Harshad or Niven series" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import itertools
def harshad(n):
    return n % sum(map(int, str(n))) == 0
hs = itertools.filterfalse(lambda n: not harshad(n), itertools.count(1))
print("first 20 Harshad numbers: " + " ".join(str(next(hs)) for _ in range(20)))
print(f"first Harshad number above 1000: {next(n for n in itertools.count(1001) if harshad(n))}")
