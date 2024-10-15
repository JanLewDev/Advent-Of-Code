with open("in1") as f:
    data = f.read()

import re

ans = 0

lines = data.split("\n")
array = [[lines[j][i] for i in range(len(lines))] for j in range(len(lines))]

def inside(x, y):
    return x >= 0 and y >= 0 and x < len(lines) and y < len(lines)

ans = 0

# for i in range(len(lines)):
#     d = dict((m.start(), m.group()) for m in re.finditer(r'\d+', lines[i]))
#     for idx, number in d.items():
#         add = False
#         if inside(i, idx-1) and array[i][idx-1] != '.' and not array[i][idx-1].isdigit():
#             add = True
        
#         for j in range(len(number)+2):
#             if inside(i-1, idx+j-1) and array[i-1][idx+j-1] != '.' and not array[i-1][idx+j-1].isdigit():
#                 add = True

#             if inside(i+1, idx+j-1) and array[i+1][idx+j-1] != '.' and not array[i+1][idx+j-1].isdigit():
#                 add = True

#         if inside(i, idx+len(number)) and array[i][idx+len(number)] != '.' and not array[i][idx+len(number)].isdigit():
#             add = True
    
#         if add:
#             ans += int(number)


gears = {}

for i in range(len(lines)):
    d = dict((m.start(), m.group()) for m in re.finditer(r'\d+', lines[i]))
    for idx, number in d.items():
        if inside(i, idx-1) and array[i][idx-1] == '*':
            if (i, idx-1) in gears:
                gears[(i, idx-1)].add(int(number))
            else:
                gears[(i, idx-1)] = set([int(number)])
        
        for j in range(len(number)+2):
            if inside(i-1, idx+j-1) and array[i-1][idx+j-1] == '*':
                if (i-1, idx+j-1) in gears:
                    gears[(i-1, idx+j-1)].add(int(number))
                else:
                    gears[(i-1, idx+j-1)] = set([int(number)])

            if inside(i+1, idx+j-1) and array[i+1][idx+j-1] == '*':
                if (i+1, idx+j-1) in gears:
                    gears[(i+1, idx+j-1)].add(int(number))
                else:
                    gears[(i+1, idx+j-1)] = set([int(number)])

        if inside(i, idx+len(number)) and array[i][idx+len(number)] == '*':
            if (i, idx+len(number)) in gears:
                gears[(i, idx+len(number))].add(int(number))
            else:
                gears[(i, idx+len(number))] = set([int(number)])
    

# print(gears)
for gear, numbers in gears.items():
    if len(numbers) == 2:
        add = 1
        for i in numbers:
            add *= i

        ans += add

print(f"answer is {ans}")
