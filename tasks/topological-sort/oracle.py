# Independent reference for "Topological sort" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import heapq
groups = [('des_system_lib', 'std synopsys std_cell_lib des_system_lib dw02 dw01 ramlib ieee'), ('dw01', 'ieee dw01 dware gtech'), ('dw02', 'ieee dw02 dware'), ('dw03', 'std synopsys dware dw03 dw02 dw01 ieee gtech'), ('dw04', 'dw04 ieee dw01 dware gtech'), ('dw05', 'dw05 ieee dware'), ('dw06', 'dw06 ieee dware'), ('dw07', 'ieee dware'), ('dware', 'ieee dware'), ('gtech', 'ieee gtech'), ('ramlib', 'std ieee'), ('std_cell_lib', 'ieee std_cell_lib'), ('synopsys', '')]
deps = {}
for lib, ds in groups:
    deps.setdefault(lib, set())
    for d in ds.split():
        deps.setdefault(d, set())
        if d != lib:
            deps[lib].add(d)
users = {n: set() for n in deps}
for lib, ds in deps.items():
    for d in ds:
        users[d].add(lib)
indeg = {n: len(ds) for n, ds in deps.items()}
ready = [n for n, k in indeg.items() if k == 0]
heapq.heapify(ready)
order = []
while ready:
    n = heapq.heappop(ready)
    order.append(n)
    for u in users[n]:
        indeg[u] -= 1
        if indeg[u] == 0:
            heapq.heappush(ready, u)
# the order is checked directly: every library comes after everything it depends on
pos = {n: i for i, n in enumerate(order)}
assert all(pos[d] < pos[lib] for lib in order for d in deps[lib])
print(" ".join(order))
print("un-orderable:" + "".join(" " + n for n in sorted(set(deps) - set(order))))
