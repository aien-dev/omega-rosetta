# Independent reference for "Hofstadter Q sequence" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
q = {1: 1, 2: 1}
def Q(n):
    # fill Q(len(q)+1) .. Q(n) in order; each term uses only earlier ones
    for m in range(len(q) + 1, n + 1):
        q[m] = q[m - q[m - 1]] + q[m - q[m - 2]]
    return q[n]
Q(100000)
print("first 10 terms: " + " ".join(str(Q(n)) for n in range(1, 11)))
print(f"the 1000th term: {Q(1000)}")
print(f"terms up to the 100000th that are less than the term before: {sum(1 for n in range(2, 100001) if q[n] < q[n - 1])}")
