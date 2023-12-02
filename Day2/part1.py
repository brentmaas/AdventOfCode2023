num_red = 12
num_green = 13
num_blue = 14
sum = 0
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        game_id = int(line.split()[1][:-1])
        sets = line[line.index(":")+2:].split(";")
        for set in sets:
            for cubes in set.strip().split(", "):
                num, colour = cubes.split(" ")
                num = int(num)
                if (colour == "red" and num > num_red) or (colour == "green" and num > num_green) or (colour == "blue" and num > num_blue):
                    game_id *= 0
        sum += game_id
print(sum)