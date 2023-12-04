with open("in1") as f:
    data = f.read()


def integers(string):
    numbers = [int(x) for x in string.split() if x.isnumeric()]
    return numbers

ans = 0

lines = data.split("\n")
games = [line.strip().split(": ") for line in lines]

cards = [1 for _ in range(len(games) + 1)]


for game in games:
    idx = integers(game[0])[0]
    rounds = game[1].split(" | ")
    rounds = [integers(i) for i in rounds]
    
    score = 0
    for num in rounds[1]:
        if num in rounds[0]:
            score += 1

    for i in range(idx+1, idx + score + 1):
            cards[i] += cards[idx]

    # if score:
    #     ans += 2 ** (score - 1)
    
    ans += cards[idx]

print(f"answer is {ans}")
