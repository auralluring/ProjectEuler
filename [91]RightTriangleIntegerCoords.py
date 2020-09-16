from itertools import permutations, combinations
size = 50

def validTriangle(px, py, qx, qy):
    if (px, py) == (0, 0) or (qx, qy) == (0, 0) or (px, py) == (qx, qy):
        return False
    elif (px, qy) == (0, 0) or (px == 0 and py == qy) or (py == 0 and px == qx) or ((px * (qx - px) + py * (qy - py)) == 0):
        return True
    else:
        return False

triangles = 0
for px in range(size + 1):
    for py in range(size + 1):
        for qx in range(size + 1):
            for qy in range(size + 1):
                if validTriangle(px, py, qx, qy) : triangles += 1
print(triangles)