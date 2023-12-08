import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict

def integers(string):
    numbers = [int(x) for x in string.split() if x.isnumeric()]
    return numbers

def p1():
    graph = {}

    ans = 0
    lines = data.split("\n\n")
    instructions, nodes = lines
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

    ans = 0
    lines = data.split("\n\n")
    instructions, nodes = lines
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
    offsets = []
    lengths = []
    for node in starts:
        visited = []
        copy = node
        step = 0
        run = True
        while copy != node or run: 
            prev = copy
            if instructions[step % len(instructions)] == 'L':
                copy = graph[copy][0]
            else:    
                copy = graph[copy][1]

            if copy in visited and prev[-1] == 'Z':
                # print(node, visited.index(copy), step)
                offsets.append(visited.index(copy))
                lengths.append(step)
                break
            visited.append(copy)
            step += 1
            run = False
        
        cycles.append(step)
        
    import math

    print(f"answer is {math.lcm(*lengths)}")


p2()