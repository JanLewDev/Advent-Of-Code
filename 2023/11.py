import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from itertools import cycle
import math

def integers(string):
    numbers = [int(x) for x in string.split()]
    return numbers

def distance(x, y):
    x1, y1 = x
    x2, y2 = y
    return abs(x1-x2) + abs(y1-y2)

def p1():
    ans = 0
    lines = data.split("\n")
    grid = [[i for i in j] for j in lines]
    rows = len(lines)
    columns = len(lines[0])


    i = 0
    while i < len(grid):
        if grid[i].count('#') == 0:
            grid.insert(i+1, ['.']*columns)
            i += 1
        i += 1
            
    
    j = 0
    while j < len(grid[0]):
        if [grid[i][j] for i in range(len(grid))].count('#') == 0:
            for i in range(len(grid)):
                grid[i].insert(j+1, '.')
            j += 1
        j += 1

    rows = len(grid)
    columns = len(grid[0])
    galaxy = []
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == '#':
                galaxy.append((i, j))

    # print('\n'.join([''.join(i) for i in grid]))

    for i in range(len(galaxy)):
        for j in range(i+1, len(galaxy)):
            ans += distance(galaxy[i], galaxy[j])
    

    print(f"answer is {ans}")


def p2():
    ans = 0
    lines = data.split("\n")
    grid = [[i for i in j] for j in lines]
    plus = defaultdict(lambda: 0)
    add = 999999
    # print('\n'.join([''.join(i) for i in grid]))

    rows = len(grid)
    columns = len(grid[0])
    galaxy = []
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == '#':
                galaxy.append((i, j))


    for i in range(len(grid)):
        if grid[i].count('#') == 0:
            for k in range(len(galaxy)):
                for m in range(k+1, len(galaxy)):
                    if (galaxy[k][0] < i and i < galaxy[m][0]) or (galaxy[m][0] < i and i < galaxy[k][0]):
                        plus[(galaxy[k], galaxy[m])] += add
            
    
    for j in range(len(grid[0])):
        if [grid[i][j] for i in range(len(grid))].count('#') == 0:
            for k in range(len(galaxy)):
                for m in range(k+1, len(galaxy)):
                    if (galaxy[k][1] < j and j < galaxy[m][1]) or (galaxy[m][1] < j and j < galaxy[k][1]):
                        plus[(galaxy[k], galaxy[m])] += add


    for i in range(len(galaxy)):
        for j in range(i+1, len(galaxy)):
            ans += distance(galaxy[i], galaxy[j])
            ans += plus[(galaxy[i], galaxy[j])]
    

    print(f"answer is {ans}")



p2()