import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from itertools import cycle

dirs = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
translation = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

def p1():
    ans = 0
    lines = data.split("\n")
    s = 1000
    trenches = [[False for _ in range(s)] for _ in range(s)]
    curr = (s//2, s//2)
    for line in lines:
        dir, n, _ = line.split(" ")
        n = int(n)
        for i in range(n):
            curr = (curr[0] + dirs[dir][0], curr[1] + dirs[dir][1])
            trenches[curr[0]][curr[1]] = True
            ans += 1
            # print(curr)

    print('\n'.join([''.join(['#' if trenches[i][j] else '.' for j in range(s)]) for i in range(s)]))
    
    def bfs(x, y):
        q = [(x, y)]
        area = 0
        visited = defaultdict(lambda: False)
        while q:
            (x, y) = q.pop(0)
            # print(x, y)
            if visited[(x, y)] or trenches[x][y]:
                continue
            visited[(x, y)] = True
            area += 1
            for i in dirs:
                q.append((x+dirs[i][0], y+dirs[i][1]))

        return area

    print(ans)
    print(f"answer is {ans + bfs(s//2+1, s//2+1)}")


def p2():
    ans = 0
    lines = data.split("\n")
    points = [(0, 0)]
    border = 0
    for line in lines:
        _, _, ins = line.split(" ")
        num = ins[2:-2]
        dirx, diry = dirs[translation[ins[-2]]]
        num = int(num, 16)
        border += num
        x, y = points[-1]
        points.append((x + dirx * num, y + diry * num))


    area = abs(sum(points[i][0] * (points[i-1][1] - points[(i+1) if i < len(points) - 1 else 0][1]) for i in range(len(points)))) // 2
    inside = area - border // 2 + 1
    
    print(f"answer is {inside + border}")

    # Later I found the shapely library
    import shapely
    polygon = shapely.Polygon(points)
    print(f"answer is {int(polygon.area + polygon.length // 2 + 1)}")

p2()