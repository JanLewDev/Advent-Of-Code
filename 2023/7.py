import sys
with open(sys.argv[1]) as f:
    data = f.read()

from collections import defaultdict, Counter
from functools import cmp_to_key


def integers(string):
    numbers = [int(x) for x in string.split() if x.isnumeric()]
    return numbers


def part1():
    ans = 0

    cards = "23456789TJQKA"

    def power(string):
        hand = [j for i, j in Counter(string).most_common()]

        match hand:
            case [5]:
                return 7
            case [4, 1]:
                return 6
            case [3, 2]:
                return 5
            case [3, 1, 1]:
                return 4
            case [2, 2, 1]:
                return 3
            case [2, 1, 1, 1]:
                return 2
            case _:
                return 1

    def compare(x, y):
        x, y = x[0], y[0]
        if power(x) == power(y):
            for i in range(5):
                if x[i] != y[i]:
                    return 1 if cards.index(x[i]) > cards.index(y[i]) else -1
        return 1 if power(x) > power(y) else -1

    lines = data.split("\n")
    hands = [line.strip().split(" ") for line in lines]
    hands = [(i[0], int(i[1])) for i in hands]

    hands = sorted(hands, key=cmp_to_key(compare))

    for i in range(len(hands)):
        ans += (i+1) * hands[i][1]

    print(f"answer is {ans}")


def part2():
    ans = 0

    cards = "J23456789TQKA"

    def power(string):
        jokers = string.count('J')
        string = string.replace('J', "")
        hand = [j for i, j in Counter(string).most_common()]
        if jokers == 5:
            return 7
        if hand[0] + jokers >= 5:
            return 7
        if hand[0] + jokers >= 4:
            return 6
        if hand == [3, 2] or (hand == [2, 2] and jokers):
            return 5
        if hand[0] + jokers >= 3:
            return 4
        if hand == [2, 2, 1] or (hand == [2, 1, 1] and jokers):
            return 3
        if hand[0] + jokers >= 2:
            return 2
        return 1
        

    def compare(x, y):
        x, y = x[0], y[0]
        if power(x) == power(y):
            for i in range(5):
                if x[i] != y[i]:
                    return 1 if cards.index(x[i]) > cards.index(y[i]) else -1
        return 1 if power(x) > power(y) else -1

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