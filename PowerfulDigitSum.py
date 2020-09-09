maximum = 0
for a in range(2, 100):
    for b in range(2, 100):
        n = str(a ** b)
        n = sum(map(int, n))
        if n > maximum:
            maximum = n
print(maximum)