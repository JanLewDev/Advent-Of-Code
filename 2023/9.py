import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from itertools import cycle
import math

def integers(string):
    numbers = [int(x) for x in string.split()]
    return numbers

def zeros(x):
    if x:
        return min([i == 0 for i in x])
    return True

def p1():
    sequences = data.split("\n")
    sequences = [integers(x) for x in sequences]
    ans = 0
    # create a list of differences between elements in each sequence
    for s in sequences:
        last = []
        while not zeros(s):
            last.append(s[-1])
            print(s)
            for i in range(len(s)-1):
                s[i] = s[i+1] - s[i]
            s.pop()
            

        print("last = ", last)
        ans += sum(last)

    print(f"answer is {ans}")


def p2():
    sequences = data.split("\n")
    sequences = [integers(x) for x in sequences]
    ans = 0
    # create a list of differences between elements in each sequence
    for s in sequences:
        first = []
        while not zeros(s):
            first.append(s[0])
            for i in range(len(s)-1):
                s[i] = s[i+1] - s[i]
            s.pop()
            
        
        first = first[::-1]
    
        
        
        curr = first[0]
        for i in range(1, len(first)):
            curr = first[i] - curr
        
        ans += curr
            
        

    print(f"answer is {ans}")


p2()