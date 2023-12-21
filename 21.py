import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict, deque
from itertools import cycle

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def p1():
    grid = [[i for i in j] for j in data.splitlines()]
    R = len(grid)
    C = len(grid[0])

    def inside(x, y):
        return 0 <= x < R and 0 <= y < C

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'S':
                start = (i, j)

    def bfs(steps):
        curr = set([start])
        for _ in range(steps):
            next = set()
            for x, y in curr:
                for d in dirs:
                    if inside(x+d[0], y+d[1]) and grid[x+d[0]][y+d[1]] != '#':
                        next.add((x+d[0], y+d[1]))
            curr = next
        return len(curr)


    print(f"answer is {bfs(64)}")


def p2():
    grid = [[i for i in j] for j in data.splitlines()]
    R = len(grid)
    C = len(grid[0])

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'S':
                start = (i, j)
                grid[i][j] = '.'


    def get_grid(x, y):
        if x >= R:
            x %= R
        if y >= C:
            y %= C
        if x < 0:
            x += ((abs(x)-1) // R + 1) * R
        if y < 0:
            y += ((abs(y)-1) // C + 1) * C

        assert 0 <= x < R and 0 <= y < C

        return grid[x][y]            

    
    def bfs(steps):
        curr = set([start])
        for _ in range(steps):
            next = set()
            for x, y in curr:
                for d in dirs:
                    if get_grid(x+d[0], y+d[1]) != '#':
                        next.add((x+d[0], y+d[1]))
            curr = next
        return len(curr)

    # print(steps % R, bfs(steps % R))
    # print(steps % R + R, bfs(steps % R + R))
    # print(steps % R + R + R, bfs(steps % R + R + R))
    # hard-coded after running the above
    seen = [3738, 33270, 92194]
    diff = [seen[i+1] - seen[i] for i in range(2)]
    a = (diff[1] - diff[0]) // 2
    b = diff[0] - 3 * a
    c = seen[0] - a - b
    print(a * 202301**2 + b * 202301 + c)

    # the answer is a quadratic function of steps, so we can use interpolation
    from scipy.interpolate import lagrange
    print(round(lagrange([65, 196, 327], seen)(26501365)))

p2()