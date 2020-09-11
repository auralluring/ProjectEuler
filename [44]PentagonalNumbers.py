pentagons = []
for i in range(1, 50000):
    pentagons += [int(i * ((3 * i) - 1) / 2)]
lowest = 999999999999999999999999999999999
for k in range(1, len(pentagons)):
    for j in range(k - 1, -1, -1):
        pk = pentagons[k]
        pj = pentagons[j]
        if pk + pj in pentagons and pk - pj in pentagons and pk - pj < lowest:
            lowest = pk - pj
print(lowest)

#done!