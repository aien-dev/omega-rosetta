# Independent reference for "Factorial" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import math
for n in range(21):
    print(f"{n}! = {math.factorial(n)}")
