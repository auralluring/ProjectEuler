from sympy import isprime
import time
percent = 100
n = 1
diagonals = 1
primes = 0
sideLength = 1
while percent >= 10:
    sideLength += 2
    diagonals += 4
    primes += sum([1 for n in range(n + sideLength-1, n + (sideLength * 4) - 4, sideLength-1) if isprime(n)])
    n += sideLength * 4 - 4
    percent = 100 * primes / diagonals
print(sideLength)

#done!