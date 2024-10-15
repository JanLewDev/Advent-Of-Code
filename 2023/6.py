import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict

def integers(string):
    numbers = [int(x) for x in string.split() if x.isnumeric()]
    return numbers

lines = data.split("\n")
_, *time = lines[0].split()
time = int(''.join(time))
_, *distance = lines[1].split()
distance = int(''.join(distance))

# Part one
# time = integers(lines[0])
# distance = integers(lines[1])

# ans = 1
# for i in range(len(time)):
#     poss = 0
#     for j in range(1, time[i]+1):
#         if j*(time[i]-j) > distance[i]:
#             poss += 1
#     ans *= poss
ans = 0
for j in range(1, time+1):
    if j*(time-j) > distance:
        ans += 1

    
print(f"answer = {ans}")