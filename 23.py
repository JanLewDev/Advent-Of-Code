import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict, deque
from itertools import cycle
import sys
sys.setrecursionlimit(10 ** 9)

dirs = {'>': [(0, 1)], '<': [(0, -1)], 'v': [(1, 0)], '.': [(0, 1), (0, -1), (1, 0), (-1, 0)], '#': []}

def p1():
    ans = 0
    grid = [[i for i in j] for j in data.splitlines()]
    R = len(grid)
    C = len(grid[0])

    def inside(x, y):
        return 0 <= x < R and 0 <= y < C
    
    # by inspection
    start = (0, 1)
    end = (R-1, C-2)

    visited = set()

    def dfs(point = start):
        if point == end:
            return 0
        
        ans = float("-inf")
        visited.add(point)
        x, y = point
        for i, j in dirs[grid[x][y]]:
            if inside(x+i, y+j) and (x+i, y+j) not in visited:
                ans = max(ans, dfs((x+i, y+j)) + 1)
        visited.remove(point)
        return ans

    print(f"answer is {dfs()}")


def p2():
    ans = 0
    grid = [[i for i in j] for j in data.splitlines()]
    R, C = len(grid), len(grid[0])
    grid = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] != '#'}

    def connected(x, y):
        return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    graph = {u: {v: 1 for v in connected(*u) if v in grid} for u in grid}

    # removing the long straights
    while 1:
        for u in graph:
            if len(graph[u]) == 2:
                v1, v2 = graph[u]
                new_length = graph[v1][u] + graph[u][v2]
                graph[v1][v2] = graph[v2][v1] = new_length

                del graph[u], graph[v1][u], graph[v2][u]
                break
        else:
            break

    
    # by inspection
    start = (0, 1)
    end = (R-1, C-2)

    visited = set()
    
    def dfs(u = start):
        if u == end:
            return 0
        
        ans = float("-inf")
        visited.add(u)
        for v, dist in graph[u].items():
            if v not in visited:
                ans = max(ans, dfs(v) + dist)
        visited.remove(u)
        return ans

    print(f"answer is {dfs()}")
    

p2()