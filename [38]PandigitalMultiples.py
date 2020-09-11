from itertools import permutations
highest = 0
perms = list(permutations("123456789"))
for i in range(len(perms)):
    perms[i] = "".join(perms[i])
for n in range(1, 10000):
    a = 1
    b = ""
    while len(b) < 9:
        b += str(a * n)
        a += 1
    
    if int(b) > highest and b in perms:
        highest = int(b)
print(highest)

#done!