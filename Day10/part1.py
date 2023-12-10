north = ["|", "L", "J"]
east = ["-", "L", "F"]
south = ["|", "7", "F"]
west = ["-", "J", "7"]

pipes = []
distances = []
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        pipes.append(line)
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
if check_target((start_pos[0] - 1, start_pos[1]), east):
    posses.append((start_pos[0] - 1, start_pos[1]))
    distances[start_pos[1]][start_pos[0]-1] = 1
if check_target((start_pos[0] + 1, start_pos[1]), west):
    posses.append((start_pos[0] + 1, start_pos[1]))
    distances[start_pos[1]][start_pos[0]+1] = 1
if check_target((start_pos[0], start_pos[1] - 1), south):
    posses.append((start_pos[0], start_pos[1] - 1))
    distances[start_pos[1]-1][start_pos[0]] = 1
if check_target((start_pos[0], start_pos[1] + 1), north):
    posses.append((start_pos[0], start_pos[1] + 1))
    distances[start_pos[1]+1][start_pos[0]] = 1

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

max_distance = 0
for distance in distances:
    max_distance = max(max_distance, max(distance))
print(max_distance)