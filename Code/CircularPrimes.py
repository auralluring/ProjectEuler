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