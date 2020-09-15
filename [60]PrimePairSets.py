"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
from sympy import primerange, isprime
from itertools import permutations
from time import time
start = time()
primes = tuple(primerange(1, 10000))


def makePairs(num):
    pairs = set()
    workingNum = primes[num]
    for i in range(num + 1, len(primes)): 
        workingI = primes[i]
        if isprime(int(str(primes[num]) + str(primes[i]))) and isprime(int(str(primes[i]) + str(primes[num]))) : pairs.add(i)
    return pairs
        

def primePairsFunc():
    lowest = 9999999999
    pairs = [0] * len(primes)
    for a in range(len(primes)):
        if primes[a] * 5 >= lowest : continue
        if pairs[a] == 0 : pairs[a] = makePairs(a)
        for b in pairs[a]:
            if primes[a] + primes[b] * 4 >= lowest : continue
            if pairs[b] == 0 : pairs[b] = makePairs(b)
            for c in pairs[b].intersection(pairs[a]):
                if primes[a] + primes[b] + primes[c] * 3 >= lowest : continue
                if pairs[c] == 0 : pairs[c] = makePairs(c)
                for d in pairs[c].intersection(pairs[b].intersection(pairs[a])):
                    if primes[a] + primes[b] + primes[c] + primes[d] * 2 >= lowest : continue
                    if pairs[d] == 0 : pairs[d] = makePairs(d)
                    for e in pairs[d].intersection(pairs[c].intersection(pairs[b].intersection(pairs[a]))):
                        if primes[a] + primes[b] + primes[c] + primes[d] + primes[e] >= lowest : continue
                        if pairs[e] == 0 : pairs[e] = makePairs(e)
                        lowest = primes[a] + primes[b] + primes[c] + primes[d] + primes[e]
    return lowest
print(primePairsFunc())
print(time() - start)

#done!