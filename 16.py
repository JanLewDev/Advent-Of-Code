import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from itertools import cycle
from copy import deepcopy



def p1():
    ans = 0
    dirs = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
    grid = [[i for i in j] for j in data.splitlines()]
    R = len(grid)
    C = len(grid[0])
    def inside(x, y):
        return 0 <= x < R and 0 <= y < C

    beams = [((0, 0), '>')]
    energized = [[False for _ in range(C)] for _ in range(R)]
    visited = [["" for _ in range(C)] for _ in range(R)]
    while beams:
        new_beams = []
        for (x, y), d in beams:
            if not inside(x, y):
                continue
            
            if visited[x][y] == d:
                continue

            visited[x][y] = d
            energized[x][y] = True

            if grid[x][y] == '/':
                if d == '^':
                    d = '>'
                elif d == '>':
                    d = '^'
                elif d == 'v':
                    d = '<'
                elif d == '<':
                    d = 'v'
            elif grid[x][y] == '\\':
                if d == '^':
                    d = '<'
                elif d == '>':
                    d = 'v'
                elif d == 'v':
                    d = '>'
                elif d == '<':
                    d = '^'
            elif grid[x][y] == '|':
                if d == '^':
                    d = '^'
                elif d == '>':
                    d = '^'
                    new_beams.append(((x+dirs['v'][0], y+dirs['v'][1]), 'v'))
                elif d == 'v':
                    d = 'v'
                elif d == '<':
                    d = 'v'
                    new_beams.append(((x+dirs['^'][0], y+dirs['^'][1]), '^'))
            elif grid[x][y] == '-':
                if d == '^':
                    d = '>'
                    new_beams.append(((x+dirs['<'][0], y+dirs['<'][1]), '<'))
                elif d == '>':
                    d = '>'
                elif d == 'v':
                    d = '<'
                    new_beams.append(((x+dirs['>'][0], y+dirs['>'][1]), '>'))
                elif d == '<':
                    d = '<'

            nx, ny = x + dirs[d][0], y + dirs[d][1]
            new_beams.append(((nx, ny), d))

        beams = new_beams
        print(beams)
        # print()
        # for i in range(R):
        #     for j in range(C):
        #         if energized[i][j]:
        #             print("#", end="")
        #         else:
        #             print(".", end="")
        #     print()

    ans = sum(sum(1 for i in j if i) for j in energized)
    print(f"answer is {ans}")


def p2():
    ans = 0
    dirs = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
    grid = [[i for i in j] for j in data.splitlines()]
    R = len(grid)
    C = len(grid[0])
    def inside(x, y):
        return 0 <= x < R and 0 <= y < C

    for i in range(R):
        beams = [((i, 0), '>')]
        energized = [[False for _ in range(C)] for _ in range(R)]
        visited = [["" for _ in range(C)] for _ in range(R)]
        while beams:
            new_beams = []
            for (x, y), d in beams:
                if not inside(x, y):
                    continue
                
                if visited[x][y] == d:
                    continue

                visited[x][y] = d
                energized[x][y] = True

                if grid[x][y] == '/':
                    if d == '^':
                        d = '>'
                    elif d == '>':
                        d = '^'
                    elif d == 'v':
                        d = '<'
                    elif d == '<':
                        d = 'v'
                elif grid[x][y] == '\\':
                    if d == '^':
                        d = '<'
                    elif d == '>':
                        d = 'v'
                    elif d == 'v':
                        d = '>'
                    elif d == '<':
                        d = '^'
                elif grid[x][y] == '|':
                    if d == '^':
                        d = '^'
                    elif d == '>':
                        d = '^'
                        new_beams.append(((x+dirs['v'][0], y+dirs['v'][1]), 'v'))
                    elif d == 'v':
                        d = 'v'
                    elif d == '<':
                        d = 'v'
                        new_beams.append(((x+dirs['^'][0], y+dirs['^'][1]), '^'))
                elif grid[x][y] == '-':
                    if d == '^':
                        d = '>'
                        new_beams.append(((x+dirs['<'][0], y+dirs['<'][1]), '<'))
                    elif d == '>':
                        d = '>'
                    elif d == 'v':
                        d = '<'
                        new_beams.append(((x+dirs['>'][0], y+dirs['>'][1]), '>'))
                    elif d == '<':
                        d = '<'

                nx, ny = x + dirs[d][0], y + dirs[d][1]
                new_beams.append(((nx, ny), d))

            beams = new_beams

        ans = max(ans, sum(sum(1 for i in j if i) for j in energized))
    
    for i in range(R):
        beams = [((i, R-1), '<')]
        energized = [[False for _ in range(C)] for _ in range(R)]
        visited = [["" for _ in range(C)] for _ in range(R)]
        while beams:
            new_beams = []
            for (x, y), d in beams:
                if not inside(x, y):
                    continue
                
                if visited[x][y] == d:
                    continue

                visited[x][y] = d
                energized[x][y] = True

                if grid[x][y] == '/':
                    if d == '^':
                        d = '>'
                    elif d == '>':
                        d = '^'
                    elif d == 'v':
                        d = '<'
                    elif d == '<':
                        d = 'v'
                elif grid[x][y] == '\\':
                    if d == '^':
                        d = '<'
                    elif d == '>':
                        d = 'v'
                    elif d == 'v':
                        d = '>'
                    elif d == '<':
                        d = '^'
                elif grid[x][y] == '|':
                    if d == '^':
                        d = '^'
                    elif d == '>':
                        d = '^'
                        new_beams.append(((x+dirs['v'][0], y+dirs['v'][1]), 'v'))
                    elif d == 'v':
                        d = 'v'
                    elif d == '<':
                        d = 'v'
                        new_beams.append(((x+dirs['^'][0], y+dirs['^'][1]), '^'))
                elif grid[x][y] == '-':
                    if d == '^':
                        d = '>'
                        new_beams.append(((x+dirs['<'][0], y+dirs['<'][1]), '<'))
                    elif d == '>':
                        d = '>'
                    elif d == 'v':
                        d = '<'
                        new_beams.append(((x+dirs['>'][0], y+dirs['>'][1]), '>'))
                    elif d == '<':
                        d = '<'

                nx, ny = x + dirs[d][0], y + dirs[d][1]
                new_beams.append(((nx, ny), d))

            beams = new_beams

        ans = max(ans, sum(sum(1 for i in j if i) for j in energized))

    for i in range(C):
        beams = [((0, i), 'v')]
        energized = [[False for _ in range(C)] for _ in range(R)]
        visited = [["" for _ in range(C)] for _ in range(R)]
        while beams:
            new_beams = []
            for (x, y), d in beams:
                if not inside(x, y):
                    continue
                
                if visited[x][y] == d:
                    continue

                visited[x][y] = d
                energized[x][y] = True

                if grid[x][y] == '/':
                    if d == '^':
                        d = '>'
                    elif d == '>':
                        d = '^'
                    elif d == 'v':
                        d = '<'
                    elif d == '<':
                        d = 'v'
                elif grid[x][y] == '\\':
                    if d == '^':
                        d = '<'
                    elif d == '>':
                        d = 'v'
                    elif d == 'v':
                        d = '>'
                    elif d == '<':
                        d = '^'
                elif grid[x][y] == '|':
                    if d == '^':
                        d = '^'
                    elif d == '>':
                        d = '^'
                        new_beams.append(((x+dirs['v'][0], y+dirs['v'][1]), 'v'))
                    elif d == 'v':
                        d = 'v'
                    elif d == '<':
                        d = 'v'
                        new_beams.append(((x+dirs['^'][0], y+dirs['^'][1]), '^'))
                elif grid[x][y] == '-':
                    if d == '^':
                        d = '>'
                        new_beams.append(((x+dirs['<'][0], y+dirs['<'][1]), '<'))
                    elif d == '>':
                        d = '>'
                    elif d == 'v':
                        d = '<'
                        new_beams.append(((x+dirs['>'][0], y+dirs['>'][1]), '>'))
                    elif d == '<':
                        d = '<'

                nx, ny = x + dirs[d][0], y + dirs[d][1]
                new_beams.append(((nx, ny), d))

            beams = new_beams

        ans = max(ans, sum(sum(1 for i in j if i) for j in energized))

    for i in range(R):
        beams = [((C-1, i), '^')]
        energized = [[False for _ in range(C)] for _ in range(R)]
        visited = [["" for _ in range(C)] for _ in range(R)]
        while beams:
            new_beams = []
            for (x, y), d in beams:
                if not inside(x, y):
                    continue
                
                if visited[x][y] == d:
                    continue

                visited[x][y] = d
                energized[x][y] = True

                if grid[x][y] == '/':
                    if d == '^':
                        d = '>'
                    elif d == '>':
                        d = '^'
                    elif d == 'v':
                        d = '<'
                    elif d == '<':
                        d = 'v'
                elif grid[x][y] == '\\':
                    if d == '^':
                        d = '<'
                    elif d == '>':
                        d = 'v'
                    elif d == 'v':
                        d = '>'
                    elif d == '<':
                        d = '^'
                elif grid[x][y] == '|':
                    if d == '^':
                        d = '^'
                    elif d == '>':
                        d = '^'
                        new_beams.append(((x+dirs['v'][0], y+dirs['v'][1]), 'v'))
                    elif d == 'v':
                        d = 'v'
                    elif d == '<':
                        d = 'v'
                        new_beams.append(((x+dirs['^'][0], y+dirs['^'][1]), '^'))
                elif grid[x][y] == '-':
                    if d == '^':
                        d = '>'
                        new_beams.append(((x+dirs['<'][0], y+dirs['<'][1]), '<'))
                    elif d == '>':
                        d = '>'
                    elif d == 'v':
                        d = '<'
                        new_beams.append(((x+dirs['>'][0], y+dirs['>'][1]), '>'))
                    elif d == '<':
                        d = '<'

                nx, ny = x + dirs[d][0], y + dirs[d][1]
                new_beams.append(((nx, ny), d))

            beams = new_beams

        ans = max(ans, sum(sum(1 for i in j if i) for j in energized))
    print(f"answer is {ans}")

p2()