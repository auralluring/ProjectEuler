"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from sympy import isprime, nextprime, sqrt

primes = [2, 3, 5, 7]

def perfect_square(num):
    num = int(num)
    root = sqrt(num)
    return root == int(root)
#print(perfect_square((9 - 7)/2))
num = 9
found = False
while not found:
    if not isprime(num):
        while primes[-1] < num:
            primes.append(nextprime(primes[-1]))
        for prime in primes[-2::-1]:
            if perfect_square((num - prime)/2):
                num += 2
                break
            elif prime == 2:
                found = True
    else:
        num += 2

print(num)