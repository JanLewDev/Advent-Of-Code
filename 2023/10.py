import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict, deque

def integers(string):
    numbers = [int(x) for x in string.split() if x.isnumeric()]
    return numbers

dirs = {(0, 1), (1, 0), (0, -1), (-1, 0)}

lines = data.split("\n")
tunnels = [[i for i in j] for j in lines]
rows = len(lines)
columns = len(lines[0])

for i in range(rows):
    for j in range(columns):
        if tunnels[i][j] == 'S':
            starting = (i, j)
            up = (tunnels[i-1][j] in "|F7")
            right = (tunnels[i][j+1] in "-J7")
            down = (tunnels[i+1][j] in "|LJ")
            left = (tunnels[i][j-1] in "-LF")
            if up and down:
                tunnels[i][j] = '|'
            elif up and right:
                tunnels[i][j] = 'L'
            elif up and left:
                tunnels[i][j] = 'J'
            elif down and right:
                tunnels[i][j] = 'F'
            elif down and left:
                tunnels[i][j] = '7'
            elif left and right:
                tunnels[i][j] = '-'

for x, y in dirs:
    if tunnels[starting[0]+x][starting[1]+y] != '.':
        next = (starting[0]+x, starting[1]+y)
        break

path = {starting}
prev = starting
while (next[0], next[1]) != starting:
    x, y = next
    path.add(next)
    # print(prev, next, tunnels[next[0]][next[1]])
    if tunnels[x][y] == '|':
        if (x+1, y) != prev:
            prev, next = next, (x+1, y)
        else:
            prev, next = next, (x-1, y)
    if tunnels[x][y] == '-':
        if (x, y+1) != prev:
            prev, next = next, (x, y+1)
        else:
            prev, next = next, (x, y-1)
    if tunnels[x][y] == 'L':
        if (x, y+1) != prev:
            prev, next = next, (x, y+1)
        else:
            prev, next = next, (x-1, y)
    if tunnels[x][y] == 'J':
        if (x, y-1) != prev:
            prev, next = next, (x, y-1)
        else:
            prev, next = next, (x-1, y)
    if tunnels[x][y] == '7':
        if (x+1, y) != prev:
            prev, next = next, (x+1, y)
        else:
            prev, next = next, (x, y-1)
    if tunnels[x][y] == 'F':
        if (x+1, y) != prev:
            prev, next = next, (x+1, y)
        else:
            prev, next = next, (x, y+1)
    
print(f"answer is {len(path) // 2}")

# visibility = {'-':'─', '|':'│', 'L': '└', 'J': '┘', '7': '┐', 'F': '┌'}
# for i in range(rows):
#     for j in range(columns):
#         if tunnels[i][j] in visibility:
#             tunnels[i][j] = visibility[tunnels[i][j]]
# print('\n'.join([''.join(i) for i in tunnels]))

# This is a much shorter solution for part two
ans = 0
for i in range(rows):
    inside = False
    for j in range(columns):
        curr = (i, j)
        if curr not in path:
            ans += inside
        elif tunnels[i][j] in "|F7":
            inside = not inside
    
print(f"answer is {ans}")  

# I left this solution here as it was my first approach
# making the new tunnels grid by extrapolating each entry to 3x3
newrows = 3*rows
newcolumns = 3*columns

new_tunnels = [['.' for i in range(newcolumns)] for j in range(newrows)]
for i in range(rows):
    for j in range(columns):
        match tunnels[i][j]:
            case 'S':
                for k in range(3):
                    for l in range(3):
                        new_tunnels[i*3+k][j*3+l] = 'S'
            case 'L':
                new_tunnels[i*3][j*3+1] = new_tunnels[i*3+1][j*3+1] = new_tunnels[i*3+1][j*3+2] = '*'
            case 'J':
                new_tunnels[i*3][j*3+1] = new_tunnels[i*3+1][j*3+1] = new_tunnels[i*3+1][j*3] = '*'
            case '7':
                new_tunnels[i*3+1][j*3] = new_tunnels[i*3+1][j*3+1] = new_tunnels[i*3+2][j*3+1] = '*'
            case 'F':
                new_tunnels[i*3+1][j*3+2] = new_tunnels[i*3+1][j*3+1] = new_tunnels[i*3+2][j*3+1] = '*'
            case '-':
                new_tunnels[i*3+1][j*3] = new_tunnels[i*3+1][j*3+1] = new_tunnels[i*3+1][j*3+2] = '*'
            case '|':
                new_tunnels[i*3][j*3+1] = new_tunnels[i*3+1][j*3+1] = new_tunnels[i*3+2][j*3+1] = '*'
            

# print('\n'.join([''.join(i) for i in new_tunnels]))
queue = deque()
visited = set()

for i in range(newrows):
    queue.append((i, 0))
    queue.append((i, newcolumns-1))
for i in range(newcolumns):
    queue.append((0, i))
    queue.append((newrows-1, i))

while queue:
    x, y = queue.popleft()
    if (x, y) in visited:
        continue
    if not 0<=x<newrows or not 0<=y<newcolumns:
        continue

    visited.add((x, y))
    if new_tunnels[x][y] == '*':
        continue

    for i in dirs:
        queue.append((x+i[0], y+i[1]))
    
ans = 0
for i in range(rows):
    for j in range(columns):
        vis = False
        for k in range(3):
            for l in range(3):
                if (i*3+k, j*3+l) in visited:
                    vis = True
        if not vis:
            ans += 1

print(f"answer is {ans}")

