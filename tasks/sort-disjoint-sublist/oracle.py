# Independent reference for "Sort disjoint sublist" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
values = [7, 6, 5, 4, 3, 2, 1, 0]
indices = [6, 1, 7]
print(*values)
print("indices:", *indices)
ix = sorted(set(indices))
for i, v in zip(ix, sorted(values[i] for i in ix)):
    values[i] = v
print(*values)
