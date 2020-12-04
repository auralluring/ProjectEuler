"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from sympy import primerange, isprime
longest = (0, 0)
limit = 1000000
primes = list(primerange(1, limit/4))

sequence = []

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        sequence = primes[i:j]
        if sum(sequence) > limit:
            break
        elif isprime(sum(sequence)) and len(sequence) > longest[0]:
            longest = (len(sequence), sum(sequence))

print(longest)