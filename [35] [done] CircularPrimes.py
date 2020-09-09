"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from sympy import primerange, isprime
def rotations(n):
    i = 1
    result = [n]
    while i < len(n):
        result += [n[i:] + n[:i]]
        i += 1 
    return list(set(result))
circles = []
primes = map(str, primerange(1000000))
for n in primes:
    n = str(n)
    if n == '197':
        pass
    if n not in circles:
        perms = rotations(n)
        if all(perm in primes for perm in perms):
            circles += perms
print(len(circles))

#done!
