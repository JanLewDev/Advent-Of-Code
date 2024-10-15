import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from itertools import cycle

def p1():
    ans = 0
    grids = data.split("\n\n")

    def mirror(grid):
        for i in range(1, len(grid)):
            upper = grid[:i][::-1]
            lower = grid[i:]

            upper = upper[:min(len(upper), len(lower))]
            lower = lower[:min(len(upper), len(lower))]

            if upper == lower:
                return i
        
        return 0
    
    for x in grids:
        grid = [[i for i in j] for j in x.splitlines()]
        # print('\n'.join([''.join(i) for i in grid]))
        ans += 100 * mirror(grid)
        ans += mirror(list(zip(*grid)))

    print(f"answer is {ans}")



def p2():
    ans = 0
    grids = data.split("\n\n")

    def mirror(grid):
        for i in range(1, len(grid)):
            upper = grid[:i][::-1]
            lower = grid[i:]

            upper = upper[:min(len(upper), len(lower))]
            lower = lower[:min(len(upper), len(lower))]
            if sum(sum(0 if a == b else 1 for a, b in zip(i, j)) for i, j in zip(upper, lower)) == 1:
                return i
        
        return 0
    
    for x in grids:
        grid = [[i for i in j] for j in x.splitlines()]
        # print('\n'.join([''.join(i) for i in grid]))
        ans += 100 * mirror(grid)
        ans += mirror(list(zip(*grid)))

    print(f"answer is {ans}")



p2()