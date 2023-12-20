import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict, deque
from itertools import cycle
from math import gcd, lcm

def p1():
    ans = [0, 0]
    modules = data.splitlines()

    config = {}
    flip_flops = {}
    conjunctions = {}
    connected_flip = {}

    for m in modules:
        name, destinations = m.split(" -> ")
        destinations = destinations.split(", ")
        if name[0] == '%':
            name = name[1:]
            flip_flops[name] = False
        elif name[0] == '&':
            name = name[1:]
            conjunctions[name] = set()
            connected_flip[name] = 0
                
        config[name] = destinations

    for i in config:
        for j in config[i]:
            if j in conjunctions:
                connected_flip[j] += 1

    # print(connected_flip)
    # print(config)

    def push():
        q = deque()
        # 0 low, 1 high
        ans[0] += 1
        for i in config["broadcaster"]:
            q.append(("broadcaster", i, False))

        while q:
            prev, curr, pulse = q.popleft()
            # print(prev, curr, pulse)
            ans[pulse] += 1
            if curr in flip_flops:
                if not pulse:
                    if not flip_flops[curr]:
                        flip_flops[curr] = True
                        for i in config[curr]:
                            q.append((curr, i, True))
                    else:
                        flip_flops[curr] = False
                        for i in config[curr]:
                            q.append((curr, i, False))

            elif curr in conjunctions:
                if pulse:
                    conjunctions[curr].add(prev)
                else:
                    if prev in conjunctions[curr]:
                        conjunctions[curr].remove(prev)
                    # conjunctions[curr].remove(prev)
                if len(conjunctions[curr]) == connected_flip[curr]:
                    for i in config[curr]:
                        q.append((curr, i, False))
                else:
                    for i in config[curr]:
                        q.append((curr, i, True))

    for i in range(1000):
        push()
    
    print(f"answer is {ans[0] * ans[1]}")


def p2():
    modules = data.splitlines()

    config = {}
    flip_flops = {}
    conjunctions = {}
    connected_flip = {}

    for m in modules:
        name, destinations = m.split(" -> ")
        destinations = destinations.split(", ")
        if name[0] == '%':
            name = name[1:]
            flip_flops[name] = False
        elif name[0] == '&':
            name = name[1:]
            conjunctions[name] = set()
            connected_flip[name] = 0
        
        if "rx" in destinations:
            second_to_last = name
        config[name] = destinations

    for i in config:
        for j in config[i]:
            if j in conjunctions:
                connected_flip[j] += 1

    # print(connected_flip)
    # print(config)
    presses = 0
    visited = {name: 0 for name, dest in config.items() if second_to_last in dest}
    cycles = {}

    while 1:
        presses += 1
        q = deque()
        # 0 low, 1 high
        for i in config["broadcaster"]:
            q.append(("broadcaster", i, False))

        while q:
            prev, curr, pulse = q.popleft()
            if curr == second_to_last and pulse:
                # print(presses)
                visited[prev] += 1

                if prev not in cycles:
                    cycles[prev] = presses
                    # print(f"cycle length for {prev} is {presses}")

                if all(visited.values()):
                    print(f"answer is {lcm(*cycles.values())}")
                    exit(0)

            # print(prev, curr, pulse)
            
            if curr in flip_flops:
                if not pulse:
                    if not flip_flops[curr]:
                        flip_flops[curr] = True
                        for i in config[curr]:
                            q.append((curr, i, True))
                    else:
                        flip_flops[curr] = False
                        for i in config[curr]:
                            q.append((curr, i, False))

            elif curr in conjunctions:
                if pulse:
                    conjunctions[curr].add(prev)
                else:
                    if prev in conjunctions[curr]:
                        conjunctions[curr].remove(prev)
                    # conjunctions[curr].remove(prev)
                if len(conjunctions[curr]) == connected_flip[curr]:
                    for i in config[curr]:
                        q.append((curr, i, False))
                else:
                    for i in config[curr]:
                        q.append((curr, i, True))

p2()