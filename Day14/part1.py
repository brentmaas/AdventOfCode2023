def north(platform):
    for y in range(1, len(platform)):
        for x in range(len(platform[0])):
            if platform[y][x] == "O":
                dest_y = y
                while dest_y > 0 and platform[dest_y-1][x] == ".":
                    dest_y -= 1
                platform[y][x], platform[dest_y][x] = platform[dest_y][x], platform[y][x]
    return platform

platform = []
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        platform.append([c for c in line])

platform = north(platform)

load = 0
for y in range(len(platform)):
    load += platform[y].count("O") * (len(platform) - y)
print(load)