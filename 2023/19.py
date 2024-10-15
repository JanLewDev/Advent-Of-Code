import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from itertools import cycle
import re

switch = {'x': 0, 'm': 1, 'a': 2, 's': 3}

def p1():
    ans = 0
    rules, parts = data.split("\n\n")
    lr = []
    mp = {}
    start = 0
    for rule in rules.splitlines():
        code, rule = rule.split("{")
        rule = rule.split(",")
        rule[-1] = rule[-1].split("}")[0]
        lr.append(rule)
        mp[code] = len(lr) - 1
        if code == "in":
            start = len(lr) - 1
        # print(code, rule)
    
    for part in parts.splitlines():
        xmas = [int(i.group()) for i in re.finditer(r'\d+', part)]
        # print(xmas)
        idx = start
        running = True
        while running:
            for i in lr[idx]:
                # print(i)
                if ">" in i:
                    a, b = i.split(":")  
                    a, d = a.split(">")
                    # print(a, b, d, xmas[switch[a]])
                    if xmas[switch[a]] > int(d):
                        if b == 'A':
                            ans += sum(xmas)
                            running = False
                            break
                        if b == 'R':
                            running = False
                            break
                        else:
                            idx = mp[b]
                            break
                        

                
                elif "<" in i:
                    a, b = i.split(":")  
                    a, d = a.split("<")
                    if xmas[switch[a]] < int(d):
                        if b == 'A':
                            ans += sum(xmas)
                            running = False
                            break
                        if b == 'R':
                            running = False
                            break
                        else:
                            idx = mp[b]
                            break
                
                else:
                    if i == 'A':
                        ans += sum(xmas)
                        running = False
                        break
                    if i == 'R':
                        running = False
                        break
                    else:
                        idx = mp[i]
                        break

    print(f"answer is {ans}")


def p2():
    ans = 0
    rules, _ = data.split("\n\n")

    workflows = {}
    for rule in rules.splitlines():
        code, rule = rule[:-1].split("{")
        rule = rule.split(",")
        workflows[code] = ([], rule[-1])
        rule.pop()
        for i in rule:
            condition, dest = i.split(":")
            key = condition[0]
            sign = condition[1]
            val = int(condition[2:])
            workflows[code][0].append((key, sign, val, dest))
        # print(code, workflows[code])

    def eval(ranges, code="in"):
        if code == "R":
            return 0
        if code == "A":
            ret = 1
            for i in ranges.values():
                ret *= (len(i) + 1)
            return ret
        
        rules, atlast = workflows[code]

        ans = 0

        for key, sign, val, dest in rules:
            r = ranges[key]
            if sign == "<":
                T = range(r.start, val - 1)
                F = range(val, r.stop)
            else:
                T = range(val + 1, r.stop)
                F = range(r.start, val)
            if T:
                copy = dict(ranges)
                copy[key] = T
                ans += eval(copy, dest)
            if F:
                ranges = dict(ranges)
                ranges[key] = F
            else:
                break
        else:
            ans += eval(ranges, atlast)
                
        return ans
    
    
    print(f"answer is {eval({key: range(1, 4000) for key in ['x', 'm', 'a', 's']})}")
    

p2()