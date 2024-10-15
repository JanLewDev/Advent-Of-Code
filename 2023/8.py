import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from itertools import cycle
import math

def integers(string):
    numbers = [int(x) for x in string.split() if x.isnumeric()]
    return numbers

def p1():
    graph = {}

    instructions, nodes = data.split("\n\n")
    nodes = nodes.split("\n")

    for node in nodes:
        vars = node.split()
        a = vars[0]
        b = vars[2][1:-1]
        c = vars[3][:-1]
        print(a, b, c)
        graph[a] = (b, c)


    node = 'AAA'
    step = 0
    while node != 'ZZZ':
        if instructions[step % len(instructions)] == 'L':
            node = graph[node][0]
        else:    
            node = graph[node][1]
        step += 1   


    print(f"answer is {step}")


def p2():
    graph = {}

    instructions, nodes = data.split("\n\n")
    nodes = nodes.split("\n")
    starts = []

    for node in nodes:
        vars = node.split()
        a = vars[0]
        b = vars[2][1:-1]
        c = vars[3][:-1]
        graph[a] = (b, c)
        if a[-1] == 'A':
            starts.append(a)


    cycles = []
    for node in starts:
        visited = []
        for steps, (idx, dir) in enumerate(cycle(enumerate(instructions))):
            prev, node = node, graph[node][dir == "R"]
            visited.append((node, idx))
            if prev[-1] == 'Z' and (node, idx) in visited:
                cycles.append(steps)
                break
            # print(visited)
        

    print(f"answer is {math.lcm(*cycles)}")


p2()