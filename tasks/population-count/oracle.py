# Independent reference for "Population count" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import itertools
pc = lambda n: format(n, "b").count("1")
print("popcount of 3^0 .. 3^29: " + " ".join(str(pc(3 ** i)) for i in range(30)))
print("first 30 evil numbers:   " + " ".join(map(str, itertools.islice((n for n in itertools.count() if pc(n) % 2 == 0), 30))))
print("first 30 odious numbers: " + " ".join(map(str, itertools.islice((n for n in itertools.count() if pc(n) % 2 == 1), 30))))
