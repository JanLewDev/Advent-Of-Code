import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict, deque
from itertools import cycle

def intersection(brick1, brick2) -> bool:
    return max(brick1[0], brick2[0]) <= min(brick1[3], brick2[3]) and max(brick1[1], brick2[1]) <= min(brick1[4], brick2[4])

def solve():
    ans = 0
    bricks = data.splitlines()
    # corner1, corner2
    bricks = [i.replace("~", ",").split(",") for i in bricks]
    bricks = [[int(i) for i in j] for j in bricks]
    N = len(bricks)
    bricks.sort(key=lambda x: x[2])

    for i, brick in enumerate(bricks):
        z_coordinate = 1
        for other in bricks[:i]:
            if intersection(brick, other):
                z_coordinate = max(z_coordinate, other[5] + 1)
        brick[5] -= brick[2]
        brick[5] += z_coordinate
        brick[2] = z_coordinate

    bricks.sort(key=lambda x: x[2])

    supports = {i: set() for i in range(N)}
    is_supported = {i: set() for i in range(N)}

    for i, upper_brick in enumerate(bricks):
        for j, lower_brick in enumerate(bricks[:i]):
            if upper_brick[2] - 1 == lower_brick[5] and intersection(upper_brick, lower_brick):
                supports[j].add(i)
                is_supported[i].add(j)
    
        
    for i in range(N):
        if all(len(is_supported[j]) > 1 for j in supports[i]):
            ans += 1

    print(f"answer is {ans}")

    ans = 0
    for i in range(N):
        only_support = [j for j in supports[i] if len(is_supported[j]) == 1]
        q = deque(only_support)
        avalanche = set(only_support)
        avalanche.add(i)

        while q:
            brick = q.popleft()
            for other in supports[brick].difference(avalanche):
                if is_supported[other].issubset(avalanche):
                    q.append(other)
                    avalanche.add(other)
        
        ans += len(avalanche) - 1
    
    print(f"answer is {ans}")

solve()