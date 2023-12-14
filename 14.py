import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from itertools import cycle

def p1():
    ans = 0
    lines = data.splitlines()
    grid = [[i for i in j] for j in lines]
    R = len(grid)
    C = len(grid[0])
    rocks = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                x, y = i, j
                while x >= 1 and grid[x-1][y] == '.':
                    x -= 1
                grid[x][y] = 'O'
                rocks.append((x, y))

    for rock in rocks:
        ans += R - rock[0]
    
    print(f"answer is {ans}")

def cycle(grid):
    # hash = tuple(tuple(i) for i in grid)
    # if hash in d:
    #     print("Found\n\n\n", idx, d[hash])
    #     return d[hash]
    # d[hash] = idx
    R = len(grid)
    C = len(grid[0])
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                x, y = i, j
                while x >= 1 and grid[x-1][y] == '.':
                    x -= 1
                grid[x][y] = 'O'
    
    
    for j in range(C):
        for i in range(R):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                x, y = i, j
                while y >= 1 and grid[x][y-1] == '.':
                    y -= 1
                grid[x][y] = 'O'
    
   
    for i in range(R-1, -1, -1):
        for j in range(C):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                x, y = i, j
                while x <= R-2 and grid[x+1][y] == '.':
                    x += 1
                grid[x][y] = 'O'

    
    for j in range(C-1, -1, -1):
        for i in range(R):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                x, y = i, j
                while y <= C-2 and grid[x][y+1] == '.':
                    y += 1
                grid[x][y] = 'O'


    return grid

d = defaultdict(int)

def p2():
    ans = 0
    tilts = 1000000000
    lines = data.splitlines()
    grid = [[i for i in j] for j in lines]
    R = len(grid)
    C = len(grid[0])
    l = []
    # cycle 108 to 150, length 42
    for i in range(109):
        grid = cycle(grid)

    left = tilts - 109
    left = left - (42 * (left // 42))
    for i in range(left):
        grid = cycle(grid)

    
    for i in range(R):
        for j in range(C):  
            if grid[i][j] == 'O':
                ans += R - i

    print(f"answer is {ans}")

p2()