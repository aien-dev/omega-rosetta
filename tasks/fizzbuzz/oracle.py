# Independent reference for "FizzBuzz" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
for n in range(1, 101):
    print("FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else n)
