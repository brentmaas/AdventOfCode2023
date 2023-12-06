sum = 0
copies = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        numbers = line[line.index(":")+2:]
        winning_numbers = [int(num) for num in numbers.split(" | ")[0].split(" ") if len(num) > 0]
        your_numbers = [int(num) for num in numbers.split(" | ")[1].split(" ") if len(num) > 0]
        matches = 0
        for num in your_numbers:
            if num in winning_numbers:
                matches += 1
        mult = copies.pop(0)
        copies.append(1)
        for i in range(matches):
            copies[i] += mult
        sum += mult * matches + 1
print(sum)