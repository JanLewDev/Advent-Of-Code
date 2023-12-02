with open("in1") as f:
    data = f.read()


def integer(string):
    number = [int(x) for x in string.split() if x.isnumeric()]
    return number[0]


ans = 0

lines = data.split("\n")
games = [line.strip().split(": ") for line in lines]
for game in games:
    idx = integer(game[0])
    rounds = game[1].split("; ")
    rounds = [i.split(", ") for i in rounds]

    # add = True
    reds = blues = greens = 0
    for round in rounds:
        for cube in round:
            if "red" in cube:
                reds = max(reds, integer(cube))
            if "green" in cube:
                greens = max(greens, integer(cube))
            if "blue" in cube:
                blues = max(blues, integer(cube))

    ans += reds * greens * blues
    # print(reds, greens, blues)

    # if add:
    #     ans += idx

print(f"answer is {ans}")
