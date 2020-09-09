from sympy import isprime
"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""

truncatablePrimes = []
n = 11
while len(truncatablePrimes) < 11:
    if isprime(n):
        num = str(n)
        guilty = False                      #this is refferring to the "innocent until proven guilty" sentiment, 
        while len(num) > 1 and not guilty:  #and has no real meaning code-wise, other than continuing with operations until its true.
            num = num[1:]                   #It was just all I could think about at the moment.
            if not isprime(int(num)):
                guilty = True
        num = str(n)
        while len(num) > 1 and not guilty:  
            num = num[:-1]                   
            if not isprime(int(num)):
                guilty = True
        if not guilty:
            truncatablePrimes.append(n)
        n += 2
    else:
        n += 2
print(sum(truncatablePrimes))