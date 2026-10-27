# Independent reference for "Sorting algorithms/Strand sort" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def strand_sort(a):
    a = list(a)
    out = []
    while a:
        strand, rest = [a[0]], []
        for v in a[1:]:
            (strand if v >= strand[-1] else rest).append(v)
        merged = []
        i = j = 0
        while i < len(out) or j < len(strand):
            if j >= len(strand) or (i < len(out) and out[i] <= strand[j]):
                merged.append(out[i]); i += 1
            else:
                merged.append(strand[j]); j += 1
        out, a = merged, rest
    return out
a = [5, 1, 4, 2, 0, 9, 6, 3, 8, 7, -2, 11]
print(*a)
s = strand_sort(a)
assert s == sorted(a)
print(*s)
