# Independent reference for "Queue/Definition" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
from collections import deque
q = deque()
def empty():
    print("empty:", "no" if q else "yes")
def push(v):
    q.append(v)
    print("push", v)
def pop():
    if not q:
        print("pop from an empty queue: error")
        return False
    print("pop", q.popleft())
    return True
empty()
for i in range(1, 7):
    push(11 * i)
for _ in range(4):
    pop()
for i in range(7, 12):
    push(-11 * i)
empty()
while pop():
    pass
empty()
