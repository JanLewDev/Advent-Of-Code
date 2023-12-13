import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from itertools import cycle
import math
import re


def p1():
    ans = 0
    k = 0
    grids = data.split("\n\n")
    for x in grids:
        grid = [[i for i in j] for j in x.splitlines()]
        R = len(grid)
        C = len(grid[0])
        # print('\n'.join([''.join(i) for i in grid]))
        for i in range(C-1):
            refl = True
            s = min(i+1, C-i-1)
            for p in range(s):      
                col1 = [grid[j][i-p] for j in range(R)]
                col2 = [grid[j][i+p+1] for j in range(R)]
                if col1 != col2:
                    refl = False
                    break

            if refl:
                ans += i+1
                print(i+1)
        

        R = len(grid)
        C = len(grid[0])
        # print('\n'.join([''.join(i) for i in grid]))
        for i in range(R-1):
            refl = True
            s = min(i+1, R-i-1)
            for p in range(s):      
                row1 = [grid[i-p][j] for j in range(C)]
                row2 = [grid[i+p+1][j] for j in range(C)]
                if row1 != row2:
                    refl = False
                    break

            if refl:
                ans += (i+1)*100
                print(i+1)
    print(f"answer is {ans}")



def p2():
    ans = 0
    k = 0
    grids = data.split("\n\n")
    for x in grids:
        grid = [[i for i in j] for j in x.splitlines()]
        R = len(grid)
        C = len(grid[0])
        # print('\n'.join([''.join(i) for i in grid]))
        for i in range(C-1):
            refl = True
            s = min(i+1, C-i-1)
            alt = False
            for p in range(s):      
                col1 = [grid[j][i-p] for j in range(R)]
                col2 = [grid[j][i+p+1] for j in range(R)]
                diff = sum(col1[k] != col2[k] for k in range(R))
                # print(col1, col2, diff)
                if diff > 0 and alt:
                    refl = False
                    break
                if diff == 1:
                    alt = True
                elif diff > 1:
                    refl = False
                    break

            if refl and alt:
                ans += i+1
                print(i+1)
        

        R = len(grid)
        C = len(grid[0])
        # print('\n'.join([''.join(i) for i in grid]))
        for i in range(R-1):
            refl = True
            s = min(i+1, R-i-1)
            alt = False
            for p in range(s):      
                row1 = [grid[i-p][j] for j in range(C)]
                row2 = [grid[i+p+1][j] for j in range(C)]
                diff = sum(row1[k] != row2[k] for k in range(C))

                # print(row1, row2, diff)
                if diff > 0 and alt:
                    refl = False
                    break
                if diff == 1:
                    alt = True
                elif diff > 1:
                    refl = False
                    break

            if refl and alt:
                ans += (i+1)*100
                print(i+1)

        print("\n")
    print(f"answer is {ans}")



p2()