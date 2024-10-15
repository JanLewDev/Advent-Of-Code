with open("in1") as f:
    data = f.read()

lines = data.split("\n")
lines = [line.strip() for line in lines]
ans = 0

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines:
    l = 0
    while l < len(line) and (not 0 <= ord(line[l]) - ord("0") <= 9):
        l += 1

    m = 9999
    idx = 0
    for i in range(9):
        if (id := line.find(digits[i])) != -1:
            if id < m:
                m = id
                idx = i

    if l < m:
        ans += 10 * (ord(line[l]) - ord("0"))
    else:
        ans += 10 * (idx + 1)

    l = len(line) - 1
    while l >= 0 and (not 0 <= ord(line[l]) - ord("0") <= 9):
        l -= 1

    m = -9999
    idx = 0
    for i in range(9):
        if (id := line.rfind(digits[i])) != -1:
            if id > m:
                m = id
                idx = i

    if l > m:
        ans += ord(line[l]) - ord("0")
    else:
        ans += idx + 1


print(f"The answer is {ans}")
