# Independent reference for "Dijkstra's algorithm" (Python 3, standard library only).
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
# checked by enumerating every simple path, not by a priority queue
adj = {"a": {"b": 7, "c": 9, "f": 14}, "b": {"c": 10, "d": 15}, "c": {"d": 11, "f": 2}, "d": {"e": 6}, "e": {"f": 9}}
for t in "bcdef":
    r = best(adj, "a", t)
    if r is None:
        print(f"a -> {t}  unreachable")
    else:
        print(f"a -> {t}  cost {r[0]}  path " + " ".join(r[1]))
