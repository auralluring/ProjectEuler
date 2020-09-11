from sympy import primerange
from itertools import permutations
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
#generate list of 4-digit primes
primes = set(map(str, primerange(1000, 10000)))
primeSet = set(["".join(sorted(str(p))) for p in primes])
#for each item in set generate permutations and find out which ones are in the prime list
for p in primeSet:
    perms = set("".join(m) for m in permutations(p))
    primePerms = sorted(map(int, perms.intersection(primes)))
    for i in range(len(primePerms)):
        for j in primePerms[:i]:
            if j - (primePerms[i] - j) in primePerms:
                print(primePerms[i], j, j - (primePerms[i] - j))

#done!