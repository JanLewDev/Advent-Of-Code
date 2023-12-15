import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from itertools import cycle

def hash(s):
    h = 0
    for i in s:
        h = ((h + ord(i)) * 17 ) % 256
    return h


def p1():
    ans = 0
    strings = data.split(",")
    for s in strings:
        ans += hash(s)
    
    print(f"answer is {ans}")


def p2():
    ans = 0
    strings = data.split(",")
    hashmap = defaultdict(lambda: [])

    for i in strings:
        if "-" in i:
            s = i[:-1]
            box = hash(s)
            for j in hashmap[box]:
                if s in j:
                    hashmap[box].remove(j)
                    break
            
        else:
            s = i.split("=")
            s, n = s[0], int(s[1])
            box = hash(s)
            ins = False
            for j in range(len(hashmap[box])):
                if s in hashmap[box][j]:
                    hashmap[box][j] = (s, n)
                    ins = True
                    break

            if not ins:
                hashmap[box].append((s, n))

    for i in range(256):
        for j in range(len(hashmap[i])):
            ans += (i+1) * (j+1) * hashmap[i][j][1]

    print(f"answer is {ans}")

p2()