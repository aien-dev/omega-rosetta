# Independent reference for "Additive primes" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
sieve = [False, False] + [True] * 498
for i in range(2, 23):
    if sieve[i]:
        sieve[i * i::i] = [False] * len(sieve[i * i::i])
add = [p for p in range(500) if sieve[p] and sieve[sum(map(int, str(p)))]]
print("additive primes below 500 (prime, and the digit sum is prime):")
for i in range(0, len(add), 10):
    print("".join(f"{p:4d}" for p in add[i:i + 10]))
print(f"count: {len(add)}")
