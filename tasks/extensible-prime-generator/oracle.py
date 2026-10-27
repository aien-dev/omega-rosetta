# Independent reference for "Extensible prime generator" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import itertools
def primes():
    # incremental sieve: each composite maps to the primes that will strike it
    d = {}
    for q in itertools.count(2):
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d.pop(q):
                d.setdefault(p + q, []).append(p)
ps = list(itertools.islice(primes(), 10000))
print("first 20 primes: " + " ".join(map(str, ps[:20])))
print("primes between 100 and 150: " + " ".join(str(p) for p in ps if 100 <= p <= 150))
print(f"number of primes between 7700 and 8000: {sum(1 for p in ps if 7700 <= p <= 8000)}")
print(f"the 10000th prime: {ps[9999]}")
