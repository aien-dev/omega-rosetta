# Independent reference for "Floyd-Warshall algorithm" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def simple_paths(adj, s, t, seen=()):
    if s == t:
        yield (s,)
        return
    for v in adj.get(s, {}):
        if v not in seen and v != s:
            for p in simple_paths(adj, v, t, seen + (s,)):
                yield (s,) + p
def best(adj, s, t):
    cands = sorted((sum(adj[p[i]][p[i + 1]] for i in range(len(p) - 1)), p) for p in simple_paths(adj, s, t))
    if not cands:
        return None
    assert len(cands) == 1 or cands[0][0] < cands[1][0], "shortest path not unique"
    return cands[0]
# checked by enumerating every simple path (there is no negative cycle), not by the triple loop
adj = {1: {3: -2}, 2: {1: 4, 3: 3}, 3: {4: 2}, 4: {2: -1}}
print("pair     dist    path")
for i in range(1, 5):
    for j in range(1, 5):
        if i != j:
            d, p = best(adj, i, j)
            print(f"{i} -> {j}{d:>6}    " + " -> ".join(map(str, p)))
