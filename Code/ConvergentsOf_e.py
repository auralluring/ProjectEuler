from math import factorial
def e(x):
    n, d = 2, 1
    for i in range(2, x + 1):
        if i % 3 == 0:
            c = 2 * (i / 3)
        else:
            c = 1
        t = d
        d = n 
        n = int(c * d + t)
        print(sum(map(int, str(n))))

(e(100))