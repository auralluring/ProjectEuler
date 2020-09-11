from math import factorial
aboveOneMillion = 0
for n in range(23, 101):
    for r in range(2, n):
        s = factorial(n)/ (factorial(r) * factorial(n - r))
        if s > 1000000:
            aboveOneMillion += 1
print(aboveOneMillion)

#done!