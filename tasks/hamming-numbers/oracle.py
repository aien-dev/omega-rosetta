# Independent reference for "Hamming numbers" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
# Cross-check, WolframLanguageEvaluator: s = Sort[Flatten[Table[2^i 3^j 5^k, {i,0,40},{j,0,30},{k,0,20}]]];
#   {Take[s, 20], s[[1691]]} -> {{1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36}, 2125764000}
import heapq
# a min-heap: pop the smallest, push its multiples, skip repeats
h, seen, out = [1], {1}, []
while len(out) < 1691:
    v = heapq.heappop(h)
    out.append(v)
    for f in (2, 3, 5):
        if v * f not in seen:
            seen.add(v * f)
            heapq.heappush(h, v * f)
print("first 20:", *out[:20])
print("1691st:", out[1690])
