import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict

def integers(string):
    numbers = [int(x) for x in string.split() if x.isnumeric()]
    return numbers

# Part one

# lines = data.split("\n\n")
# seeds = integers(lines[0])

# mapping = [lines[i].split("\n") for i in range(1, len(lines))]
# for i in range(len(mapping)):
#     for j in range(1, len(mapping[i])):
#         mapping[i][j] = integers(mapping[i][j])

# ans = []
# for seed in seeds:
#     print(f"new seed {seed}")
#     for i in range(len(mapping)):
#         print(f"i {i}, seed beg {seed}")
#         for j in range(1, len(mapping[i])):
#             if mapping[i][j][1] <= seed <= (mapping[i][j][1] + mapping[i][j][2]):
#                 seed = mapping[i][j][0] + (seed - mapping[i][j][1])
#                 break
#         print(f"i {i}, seed end {seed}")
    
#     print(f"end of this seed {seed}")
#     ans += [seed]
    
# print(min(ans))

seeds, *mapping = data.split("\n\n")
seeds = integers(seeds)
seeds = [range(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

for m in mapping:
    text, *ranges = m.split("\n")
    ranges = [integers(i) for i in ranges]
    ranges = [(range(x, x + y), range(y, y + z)) for x, y, z in ranges]
    next_seeds = []
    for seed in seeds:
        for destination, source in ranges:
            diff = destination.start - source.start
            if seed.stop <= source.start or source.stop <= seed.start:
                continue

            both = range(max(seed.start, source.start), min(seed.stop, source.stop))
            left = range(seed.start, both.start)
            right = range(both.stop, seed.stop)
            if left:
                seeds.append(left)
            if right:
                seeds.append(right)
            
            next_seeds.append(range(both.start + diff, both.stop + diff))
            break
        else:
            next_seeds.append(seed)

    seeds = next_seeds
    
print(min(i.start for i in next_seeds))