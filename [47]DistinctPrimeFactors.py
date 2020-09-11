"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

def isPrime(num):
    if num % 2 == 0 and num != 2:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True
def factor(num):
    factors = []
    if isPrime(num):
        return [num]
    for x in range(2, int(num/2) + 1):
        if num % x == 0:
            if isPrime(x) == True:
                factors.append(x)
            else:
                factor(x)
    return factors

numList = [1, 2, 3, 4]
factorList = [[1], [2], [3], [2]]

while len(factorList[0]) < 4 or len(factorList[1]) < 4 or len(factorList[2]) < 4 or len(factorList[3]) < 4:
    numList[0], numList[1], numList[2], numList[3] = numList[1], numList[2], numList[3], numList[3] + 1
    factorList[0], factorList[1], factorList[2] = factorList[1], factorList[2], factorList[3]
    factorList[3] = factor(numList[3])

print(numList)

#done!