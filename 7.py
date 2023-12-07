import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict
from functools import cmp_to_key


def integers(string):
    numbers = [int(x) for x in string.split() if x.isnumeric()]
    return numbers


def part1():
    ans = 0

    cards = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13, 'B': 14}


    def power(string):
        d1 = defaultdict(int)
        for card in cards:
            if string.count(card) == 5:
                return 7
            elif string.count(card) == 4:
                return 6
            
            if card in string:
                d1[card] += string.count(card)
        
        mid = list(d1.values())
        
        if 2 in mid and 3 in mid:
            return 5
        if 3 in mid:
            return 4
        if mid.count(2) == 2:
            return 3
        if 2 in mid:
            return 2
        return 1

    def compare(x, y):
        hand1, hand2 = x[0], y[0]
        if power(hand1) == power(hand2):
            for i in range(5):
                if hand1[i] != hand2[i]:
                    return 1 if cards[hand1[i]] > cards[hand2[i]] else -1
        return 1 if power(hand1) > power(hand2) else -1

    lines = data.split("\n")
    hands = [line.strip().split(" ") for line in lines]
    hands = [(i[0], int(i[1])) for i in hands]

    hands = sorted(hands, key=cmp_to_key(compare))

    for i in range(len(hands)):
        ans += (i+1) * hands[i][1]



    print(f"answer is {ans}")


def part2():
    ans = 0

    cards = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 11, 'K': 12, 'A': 13, 'B': 14}

    def power(string):
        d1 = defaultdict(int)
        for card in cards:
            if string.count(card) == 5:
                return 7
            
            if card in string:
                d1[card] += string.count(card)
        
        mid = list(d1.values())
        # print(string, mid)
        if d1['J']:
            mid.remove(d1['J'])

        scores = set()
        for card in cards:
            if card != 'J':
                if string.count(card) + d1['J'] == 5:
                    scores.add(7)
                if string.count(card) + d1['J'] == 4:
                    scores.add(6)
        
        if scores:
            return max(scores)
        
        if 2 in mid and 3 in mid:
            return 5
        if mid.count(2) == 2 and d1['J'] >= 1:
            return 5
        if 1 in mid and 2 in mid and d1['J'] >= 2:
            return 5
        if 3 in mid:
            return 4
        if 2 in mid and d1['J'] >= 1:
            return 4
        if 1 in mid and d1['J'] >= 2:
            return 4
        if mid.count(2) == 2:
            return 3
        if 2 in mid:
            return 2
        if 1 in mid and d1['J'] >= 1:
            return 2
        return 1

    def compare(x, y):
        hand1, hand2 = x[0], y[0]
        if power(hand1) == power(hand2):
            for i in range(5):
                if hand1[i] != hand2[i]:
                    return 1 if cards[hand1[i]] > cards[hand2[i]] else -1
        return 1 if power(hand1) > power(hand2) else -1

    lines = data.split("\n")
    hands = [line.strip().split(" ") for line in lines]
    hands = [(i[0], int(i[1])) for i in hands]

    # for i in hands:
    #     print(i[0], power(i[0]))

    hands = sorted(hands, key=cmp_to_key(compare))

    for i in range(len(hands)):
        ans += (i+1) * hands[i][1]

    print(f"answer is {ans}")


part2()