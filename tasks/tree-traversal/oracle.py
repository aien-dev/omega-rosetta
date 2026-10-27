# Independent reference for "Tree traversal" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
from collections import deque
tree = (1, (2, (4, (7, None, None), None), (5, None, None)), (3, (6, (8, None, None), (9, None, None)), None))
def pre(t):
    return [] if t is None else [t[0]] + pre(t[1]) + pre(t[2])
def ino(t):
    return [] if t is None else ino(t[1]) + [t[0]] + ino(t[2])
def post(t):
    return [] if t is None else post(t[1]) + post(t[2]) + [t[0]]
def level(t):
    out, q = [], deque([t])
    while q:
        n = q.popleft()
        if n:
            out.append(n[0]); q.extend(n[1:])
    return out
print("preorder:   ", *pre(tree))
print("inorder:    ", *ino(tree))
print("postorder:  ", *post(tree))
print("level-order:", *level(tree))
