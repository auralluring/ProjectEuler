triangles, pentagons, hexagons = [], [], []
for i in range(1, 100000):
    triangles += [i * (i + 1) / 2]
    pentagons += [int(i * ((3 * i) - 1) / 2)]
    hexagons += [int(i * ((2 * i) - 1))]

for h in hexagons[143:]:
    if h in triangles and h in pentagons:
        print(h)
        break
