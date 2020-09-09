n, d = 1, 1
f = 0
for _ in range(1000):
    n, d = n + 2 * d, n + d
    if len(str(n)) > len(str(d)):
        f += 1
print(f)