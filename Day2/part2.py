sum = 0
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        sets = line[line.index(":")+2:].split(";")
        nums = {"red": None, "green": None, "blue": None}
        for set in sets:
            for cubes in set.strip().split(", "):
                num, colour = cubes.split(" ")
                num = int(num)
                nums[colour] = num if nums[colour] is None else max(num, nums[colour])
        sum += nums["red"] * nums["green"] * nums["blue"]
print(sum)