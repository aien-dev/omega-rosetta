# Independent reference for "Fibonacci n-step number sequences" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
names = {2: "fibonacci: ", 3: "tribonacci:", 4: "tetranacci:", 5: "pentanacci:", 6: "hexanacci: ",
         7: "heptanacci:", 8: "octonacci: ", 9: "nonanacci: ", 10: "decanacci: "}
def nstep(seed, n, count):
    a = list(seed)
    while len(a) < count:
        a.append(sum(a[-n:]))
    return a[:count]
# the n-step sequence is seeded with the first n terms of the (n-1)-step one, starting from 1, 1
seed = [1, 1]
for n in range(2, 11):
    if n > 2:
        seed = nstep(seed, n - 1, n)
    print(names[n] + "".join(f" {v}" for v in nstep(seed, n, 15)))
print("lucas:     " + "".join(f" {v}" for v in nstep([2, 1], 2, 15)))
