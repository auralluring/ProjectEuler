"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""
from sympy import isprime, nextprime
from itertools import permutations
def next(num, digit, i):
    if i >= len(num) - 1:
        return 0
    i += 1
    while num[i] != digit and i < len(num) - 1:
        i += 1
    if num[i] != digit:
        return 0
    return i
def replace_digit(n, digit, which):
    new = []
    
    for x in range(10):
        num = list(str(n)[:])
        i = num.index(str(digit))
    
        for j in range(len(which)):
            if int(which[j]):
                num[i] = str(x)
            if j < len(which) - 1:
                i = next(num, str(digit), i)

        new.append(int("".join(num)))
    return list(filter(isprime, new))

#print(replace_digit(56003, 0, "01"))


def equal_length(lst):
    lst = list(map(str, lst))
    length = len(lst[0])
    for x in lst:
        if not len(x) == length:
            return False
    return True
#print(equal_length([56003, 56113, 56333, 56443, 56663, 56773, 56993]))
lst = []
found = False
result = (0, 0)
prime = 11
while not found:
    #prime = 56003
    length = 0
    for digit in set(str(prime)):
        count = str(prime).count(digit)
        for c in range(1, count + 1):
            perms = set(permutations(list("1" * c + "0" * (count - c))))
            for perm in perms:
                perm = "".join(perm)
                lst = replace_digit(prime, digit, perm)
                length = len(lst)
                if length == 8 and equal_length(lst):
                    result = (min(lst), length)
                    found = True
                    break
            if found:
                break
        if found:
            break

    prime = nextprime(prime)
print(result, lst)