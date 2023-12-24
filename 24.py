import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict, deque
from itertools import cycle
import sympy


def p1():
    ans = 0
    hailstones = [[int(i) for i in j.replace(" @", ',').split(',')] for j in data.splitlines()]
    limd, limu = 2 * 10 ** 14, 4 * 10 ** 14
    # limd, limu = 7, 27

    for i in range(len(hailstones)):
        for j in range(i+1, len(hailstones)):
            x1, y1, _, u1, v1, _ = hailstones[i]
            x2, y2, _, u2, v2, _ = hailstones[j]
            det = -u1*v2 + u2*v1
            if det == 0:
                # no intersection
                # print(f"no intersection {hailstones[i]} {hailstones[j]}")
                continue
            Δx = x2 - x1
            Δy = y2 - y1
            a = (-v2*Δx + u2*Δy) / det
            b = (-v1*Δx + u1*Δy) / det
            intersectionx = x1 + a*u1
            intersectiony = y1 + a*v1
            # print(hailstones[i], hailstones[j], intersectionx, intersectiony, a, b)
            if limd <= intersectionx <= limu and limd <= intersectiony <= limu and a >= 0 and b >= 0:
                ans += 1

    print(f"answer is {ans}")


def p2():
    hailstones = [[int(i) for i in j.replace(" @", ',').split(',')] for j in data.splitlines()]
    
    # rock's position and velocity
    rx, ry, rz, rvx, rvy, rvz = sympy.symbols("rx, ry, rz, rvx, rvy, rvz")

    equations = []

    for i in range(len(hailstones)):
        x, y, z, vx, vy, vz = hailstones[i]
        # make the ratios equal
        equations.append((rx - x) * (vy - rvy) - (ry - y) * (vx - rvx))
        equations.append((ry - y) * (vz - rvz) - (rz - z) * (vy - rvy))

    solution = sympy.solve(equations)
    print(solution)
    print(f"answer is {solution[0][rx] + solution[0][ry] + solution[0][rz]}")

    

p2()