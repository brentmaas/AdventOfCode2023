with open("Input.txt", "r") as f:
    sum = 0
    while line := f.readline():
        i_first = 0
        i_last = len(line) - 1
        while not line[i_first].isdigit():
            i_first += 1
        while not line[i_last].isdigit():
            i_last -= 1
        sum += int(f"{line[i_first]}{line[i_last]}")
print(sum)