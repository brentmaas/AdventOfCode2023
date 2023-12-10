north = ["|", "L", "J"]
east = ["-", "L", "F"]
south = ["|", "7", "F"]
west = ["-", "J", "7"]

pipes = []
distances = []
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        pipes.append([c for c in line])
        distances.append([-1 for _ in range(len(line))])
        if "S" in line:
            start_pos = (line.index("S"), len(pipes) - 1)
            distances[start_pos[1]][start_pos[0]] = 0

def check_source(pos, type):
    return pipes[pos[1]][pos[0]] in type

def check_target(pos, type):
    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(pipes[0]) or pos[1] >= len(pipes):
        return False
    return distances[pos[1]][pos[0]] < 0 and pipes[pos[1]][pos[0]] in type

posses = []
start_south = False
start_north = False
start_east = False
start_west = False
if check_target((start_pos[0] - 1, start_pos[1]), east):
    posses.append((start_pos[0] - 1, start_pos[1]))
    distances[start_pos[1]][start_pos[0]-1] = 1
    start_west = True
if check_target((start_pos[0] + 1, start_pos[1]), west):
    posses.append((start_pos[0] + 1, start_pos[1]))
    distances[start_pos[1]][start_pos[0]+1] = 1
    start_east = True
if check_target((start_pos[0], start_pos[1] - 1), south):
    posses.append((start_pos[0], start_pos[1] - 1))
    distances[start_pos[1]-1][start_pos[0]] = 1
    start_north = True
if check_target((start_pos[0], start_pos[1] + 1), north):
    posses.append((start_pos[0], start_pos[1] + 1))
    distances[start_pos[1]+1][start_pos[0]] = 1
    start_south = True

if start_south:
    if start_north:
        pipes[start_pos[1]][start_pos[0]] = "|"
    if start_west:
        pipes[start_pos[1]][start_pos[0]] = "7"
    if start_east:
        pipes[start_pos[1]][start_pos[0]] = "F"
if start_north:
    if start_west:
        pipes[start_pos[1]][start_pos[0]] = "J"
    if start_east:
        pipes[start_pos[1]][start_pos[0]] = "L"
if start_west and start_east:
    pipes[start_pos[1]][start_pos[0]] = "-"

while len(posses) > 0:
    curr_pos = posses.pop(0)
    if check_source(curr_pos, west) and check_target((curr_pos[0] - 1, curr_pos[1]), east):
        posses.append((curr_pos[0] - 1, curr_pos[1]))
        distances[curr_pos[1]][curr_pos[0]-1] = distances[curr_pos[1]][curr_pos[0]] + 1
    elif check_source(curr_pos, east) and check_target((curr_pos[0] + 1, curr_pos[1]), west):
        posses.append((curr_pos[0] + 1, curr_pos[1]))
        distances[curr_pos[1]][curr_pos[0]+1] = distances[curr_pos[1]][curr_pos[0]] + 1
    elif check_source(curr_pos, north) and check_target((curr_pos[0], curr_pos[1] - 1), south):
        posses.append((curr_pos[0], curr_pos[1] - 1))
        distances[curr_pos[1]-1][curr_pos[0]] = distances[curr_pos[1]][curr_pos[0]] + 1
    elif check_source(curr_pos, south) and check_target((curr_pos[0], curr_pos[1] + 1), north):
        posses.append((curr_pos[0], curr_pos[1] + 1))
        distances[curr_pos[1]+1][curr_pos[0]] = distances[curr_pos[1]][curr_pos[0]] + 1

enclosed = 0
should_count = False
for y in range(len(pipes)):
    for x in range(len(pipes[0])):
        if should_count:
            if distances[y][x] < 0:
                enclosed += 1
            elif pipes[y][x] == "|":
                should_count = False
            elif pipes[y][x] in east and (pipes[y][x] in south or pipes[y][x] in north):
                should_count = False
                was_north = pipes[y][x] in north
            elif (pipes[y][x] in north and was_north) or (pipes[y][x] in south and not was_north):
                should_count = False
        elif distances[y][x] >= 0:
            if pipes[y][x] == "|":
                should_count = True
            elif pipes[y][x] in east and (pipes[y][x] in south or pipes[y][x] in north):
                should_count = True
                was_north = pipes[y][x] in north
            elif (pipes[y][x] in north and was_north) or (pipes[y][x] in south and not was_north):
                should_count = True
print(enclosed)