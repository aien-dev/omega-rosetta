# Independent reference for "Hofstadter Figure-Figure sequences" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import itertools

def figure_figure():
    # R(n) = R(n-1) + S(n-1); S runs through the positive integers that R skips
    r, rs, s = 1, {1}, 2
    yield r, s
    while True:
        r += s
        rs.add(r)
        s = next(c for c in itertools.count(s + 1) if c not in rs)
        yield r, s

R = [r for r, _ in itertools.islice(figure_figure(), 40)]
S = [s for _, s in itertools.islice(figure_figure(), 960)]
print("R(1) to R(10): " + " ".join(map(str, R[:10])))
ok = sorted(R + S) == list(range(1, 1001))
print("first 40 R and first 960 S cover 1..1000 exactly once: " + ("yes" if ok else "no"))
