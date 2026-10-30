# Independent reference for "Dutch national flag problem" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
M = 2 ** 64
x = 0
def rnd():
    global x
    x = (x * 6364136223846793005 + 1442695040888963407) % M
    return x >> 33
names = ["red", "white", "blue"]
while True:
    balls = [rnd() % 3 for _ in range(12)]
    if balls != sorted(balls):
        break
for b in (balls, sorted(balls)):
    print(*(names[c] for c in b))
    print("in flag order:", "yes" if b == sorted(b) else "no")
