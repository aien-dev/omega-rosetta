# Independent reference for "Stack" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
stack = []
def empty():
    print("empty:", "no" if stack else "yes")
empty()
for v in (10, -20, 30):
    stack.append(v)
    print("push", v)
print("peek", stack[-1])
print("size", len(stack))
print("pop", stack.pop())
print("pop", stack.pop())
empty()
print("pop", stack.pop())
empty()
