# Independent reference for "Power set" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# built by doubling: the subsets without the next element, then the same subsets with it added,
# which lists them in binary-counting order of their membership masks
subsets = [[]]
for x in [1, 2, 3, 4]:
    subsets += [s + [x] for s in subsets]
for s in subsets:
    print("{" + ", ".join(map(str, s)) + "}")
print("subsets:", len(subsets))
