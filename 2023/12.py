import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from itertools import cycle, chain, combinations
from functools import lru_cache
import math
import re

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def check(code, num):
    curr = 0
    
    blocks = []
    for i in range(len(code)):
        if code[i] == '#':
            curr += 1
        else:
            if curr:
                blocks.append(curr)
                curr = 0

    if curr:
        blocks.append(curr)
    
    # print(blocks, num)

    if blocks != num:
        return False
    # print(code, num)
    return True
        

def p1():
    ans = 0
    k = 0
    lines = data.split("\n")
    for line in lines:
        code, num = line.split(" ")
        num = [int(m.group()) for m in re.finditer(r'\d+', line)]
        q = [i for i in range(len(code)) if code[i] == '?']
        p = list(powerset(q))
        x = 0
        for sub in p:
            cop = list(code[:])
            for i in range(len(cop)):
                if i in sub:
                    cop[i] = '#'
            if check(cop, num):
                x += 1
            # print(cop, num)

        ans += x
        k += 1
        print(k)               
    

    print(f"answer is {ans}")

@lru_cache
def dp(code, num, currentBlock=None):
    if not num and not currentBlock:
        return "#" not in code
    
    if not code:
        if not currentBlock:
            return len(num) == 0
        else:
            return 0
        
    match code[0], currentBlock:
        case ".", None | 0:
            return dp(code[1:], num)
        case ".", _:
            return 0
        
        case "#", None:
            return dp(code, num[1:], currentBlock=num[0])
        case "#", 0:
            return 0
        case "#", _:
            return dp(code[1:], num, currentBlock=currentBlock-1)
        
        case "?", None:
            return dp(code[1:], num) + dp(code, num[1:], currentBlock=num[0])
        case "?", 0:
            return dp(code[1:], num)
        case "?", _:
            return dp(code[1:], num, currentBlock=currentBlock-1)


def p2():
    ans = 0
    k = 0
    lines = data.split("\n")
    for line in lines:
        code, num = line.split(" ")
        code = "?".join([code] * 5)
        num = tuple([int(i) for i in num.split(",")] * 5)

        ans += dp(code, num) 
        k += 1
        print(k)           
    

    print(f"answer is {ans}")



p2()