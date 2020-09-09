#make function  that take in number n and returns all pandigitals of n that are prime. for loop to iterate through n from 1 to 9, but in reverse 
from itertools import permutations
from sympy import isprime
def pandigitalPrimes(n):
    base = "123456789"
    base = base[:n]
    perms = list(permutations(base))
    for i in range(len(perms)):
        perms[i] = "".join(perms[i])
    perms = map(int, perms)
    return list(filter(isprime, perms))
print(pandigitalPrimes(7))
for n in range(1, 9):
    panPrimes = pandigitalPrimes(n)
    if len(panPrimes):
        maximum = max(panPrimes)
print(maximum)