import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from itertools import cycle
import heapq

moves = {(0, 1): [(-1, 0), (1, 0)], (0, -1): [(1, 0), (-1, 0)], (-1, 0): [(0, -1), (0, 1)], (1, 0): [(0, 1), (0, -1)]}

def solve():
    ans = 0
    grid = [[int(i) for i in j] for j in data.splitlines()]
    R = len(grid)
    C = len(grid[0])

    def inside(x, y):
        return 0 <= x < R and 0 <= y < C
    
    def dijkstra(minstreak, maxstreak):
        # dist, x, y, dirx, diry, streak
        pq = [(0, 0, 0, 0, 1, 0), (0, 0, 0, 1, 0, 0)]
        vis = set()

        while pq:
            dist, x, y, dirx, diry, streak = heapq.heappop(pq)
            if x == R-1 and y == C-1 and streak >= minstreak:
                return dist
            
            if (x, y, dirx, diry, streak) in vis:
                continue

            vis.add((x, y, dirx, diry, streak))
            
            if streak < maxstreak:
                if inside(x+dirx, y+diry):
                    heapq.heappush(pq, (dist+grid[x+dirx][y+diry], x+dirx, y+diry, dirx, diry, streak+1))

            if streak >= minstreak or (x, y) == (0, 0):
                for move in moves[(dirx, diry)]:
                    if inside(x+move[0], y+move[1]):
                        heapq.heappush(pq, (dist+grid[x+move[0]][y+move[1]], x+move[0], y+move[1], move[0], move[1], 1))


    print(f"answer is {dijkstra(1, 3)}")
    print(f"answer is {dijkstra(4, 10)}")

solve()
