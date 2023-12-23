def north(platform):
    for y in range(1, len(platform)):
        for x in range(len(platform[0])):
            if platform[y][x] == "O":
                dest_y = y
                while dest_y > 0 and platform[dest_y-1][x] == ".":
                    dest_y -= 1
                platform[y][x], platform[dest_y][x] = platform[dest_y][x], platform[y][x]
    return platform

def west(platform):
    for x in range(1, len(platform[0])):
        for y in range(len(platform)):
            if platform[y][x] == "O":
                dest_x = x
                while dest_x > 0 and platform[y][dest_x-1] == ".":
                    dest_x -= 1
                platform[y][x], platform[y][dest_x] = platform[y][dest_x], platform[y][x]
    return platform

def south(platform):
    for y in range(len(platform) - 2, -1, -1):
        for x in range(len(platform[0])):
            if platform[y][x] == "O":
                dest_y = y
                while dest_y < len(platform) - 1 and platform[dest_y+1][x] == ".":
                    dest_y += 1
                platform[y][x], platform[dest_y][x] = platform[dest_y][x], platform[y][x]
    return platform

def east(platform):
    for x in range(len(platform[0]) - 2, -1, -1):
        for y in range(len(platform)):
            if platform[y][x] == "O":
                dest_x = x
                while dest_x < len(platform[0]) - 1 and platform[y][dest_x+1] == ".":
                    dest_x += 1
                platform[y][x], platform[y][dest_x] = platform[y][dest_x], platform[y][x]
    return platform

def copy_platform(platform):
    new_platform = []
    for row in platform:
        new_platform.append(row.copy())
    return new_platform

platform = []
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        platform.append([c for c in line])

previous_platforms = [copy_platform(platform)]

cycles = 1000000000
for _ in range(cycles):
    platform = north(platform)
    platform = west(platform)
    platform = south(platform)
    platform = east(platform)
    
    if platform in previous_platforms:
        break
    
    previous_platforms.append(copy_platform(platform))

cycle_start_index = previous_platforms.index(platform)
final_index = cycle_start_index + ((cycles - cycle_start_index) % (len(previous_platforms) - cycle_start_index))
platform = previous_platforms[final_index]

load = 0
for y in range(len(platform)):
    load += platform[y].count("O") * (len(platform) - y)
print(load)