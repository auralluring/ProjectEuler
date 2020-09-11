from math import factorial
def digitFactorial(n):
    return sum([factorial(d) for d in map(int, str(n))])
sixtyTerms = 0
for n in range(1, 1000000):
    chain = []
    while n not in chain:
        chain += [n]
        n = digitFactorial(n)
    if len(chain) == 60:
        sixtyTerms += 1
print(sixtyTerms)

#done!