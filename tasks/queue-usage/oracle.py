# Independent reference for "Queue/Usage" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
queue = []
def empty():
    print("empty:", "no" if queue else "yes")
def push(v):
    queue.append(v)
    print("push", v)
def pop():
    if not queue:
        print("pop from an empty queue: error")
    else:
        print("pop", queue.pop(0))
empty()
push(1); push(2); push(3)
pop()
empty()
push(4)
pop(); pop(); pop()
empty()
pop()
