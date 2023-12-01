digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def isdigit(line, index):
    if line[index].isdigit():
        return True
    for digit in digits:
        if len(line) > index + len(digit) and line[index:index+len(digit)] == digit:
            return True
    return False

def getdigit(line, index):
    if line[index].isdigit():
        return int(line[index])
    for i in range(len(digits)):
        if len(line) > index + len(digits[i]) and line[index:index+len(digits[i])] == digits[i]:
            return i + 1

with open("Input.txt", "r") as f:
    sum = 0
    while line := f.readline():
        i_first = 0
        i_last = len(line) - 1
        while not isdigit(line, i_first):
            i_first += 1
        while not isdigit(line, i_last):
            i_last -= 1
        sum += int(f"{getdigit(line, i_first)}{getdigit(line, i_last)}")
print(sum)