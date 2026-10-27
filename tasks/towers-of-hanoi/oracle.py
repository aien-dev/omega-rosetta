# Independent reference for "Towers of Hanoi" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
def hanoi(n, src, dst, via):
    if n:
        hanoi(n - 1, src, via, dst)
        print(f"Move disk {n} from pole {src} to pole {dst}")
        hanoi(n - 1, via, dst, src)
hanoi(4, 1, 3, 2)
