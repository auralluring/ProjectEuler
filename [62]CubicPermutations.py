"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

from itertools import permutations
from numpy import cbrt


def cubic_permutations_old(amount_to_match: int) -> str:
    matches : int = 0
    base : int = 1
    cubes = []
    while matches != amount_to_match:
        matches = 1
        base += 1
        base_cubed : int = cube(base)
        cubes.append(base_cubed)
        perms = set(permutations(str(base_cubed)))
        lowest_cubic_perm : int = -1
        for perm in perms:
            perm = int("".join(perm))
            if perm == base_cubed or len(str(perm)) != len(str(base_cubed)): continue
            if perm in cubes: 
                matches += 1
                if perm < lowest_cubic_perm or lowest_cubic_perm == -1:
                    lowest_cubic_perm = perm
        
        if base % 100 == 0:
            print("At %i" % base)
    return "%i" % (lowest_cubic_perm)


def cubic_permutations(amount_to_match: int) -> int:
    if amount_to_match == 0:
        return 0
    if amount_to_match == 1:
        return 8
    base : int = 2
    cubes = {}
    digits = 1
    while True:
        permutation_key = sort_digits(base ** 3)
        if len(permutation_key) > digits:
            matches = []
            for key in cubes:
                if cubes[key]["matches"] == amount_to_match:
                    matches.append(cubes[key]["smallest"])
            if len(matches): return min(matches)
            digits = len(permutation_key)
            cubes.clear()
        if permutation_key in cubes:
            cubes[permutation_key]["matches"] += 1
        else:
            cubes[permutation_key] = {
                "matches": 1,
                "smallest": base ** 3
            }

        base += 1


def sort_digits(num: int) -> str:
    num = str(num)
    return "".join(sorted(str(num)))


def cube(num: int) -> int:
    return num ** 3


print(cubic_permutations(5))