grid = []
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        grid.append(line)

# /
mirror1 = {(1, 0): (0, -1), (-1, 0): (0, 1), (0, 1): (-1, 0), (0, -1): (1, 0)}
# \
mirror2 = {(1, 0): (0, 1), (-1, 0): (0, -1), (0, 1): (1, 0), (0, -1): (-1, 0)}
# |
splitter1 = {(1, 0): [(0, 1), (0, -1)], (-1, 0): [(0, 1), (0, -1)], (0, 1): [(0, 1)], (0, -1): [(0, -1)]}
# -
splitter2 = {(1, 0): [(1, 0)], (-1, 0): [(-1, 0)], (0, 1): [(1, 0), (-1, 0)], (0, -1): [(1, 0), (-1, 0)]}

energised = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
beams = [(0, 0, 1, 0)]
directions_seen = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]
while len(beams) > 0:
    x, y, dx, dy = beams.pop(0)
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or (dx, dy) in directions_seen[y][x]:
        continue
    energised[y][x] = True
    directions_seen[y][x].append((dx, dy))
    if grid[y][x] == ".":
        beams.append((x + dx, y + dy, dx, dy))
    elif grid[y][x] == "/":
        ndx, ndy = mirror1[(dx, dy)]
        beams.append((x + ndx, y + ndy, ndx, ndy))
    elif grid[y][x] == "\\":
        ndx, ndy = mirror2[(dx, dy)]
        beams.append((x + ndx, y + ndy, ndx, ndy))
    elif grid[y][x] == "|":
        for ndx, ndy in splitter1[(dx, dy)]:
            beams.append((x + ndx, y + ndy, ndx, ndy))
    elif grid[y][x] == "-":
        for ndx, ndy in splitter2[(dx, dy)]:
            beams.append((x + ndx, y + ndy, ndx, ndy))

energy_sum = 0
for row in energised:
    energy_sum += sum(row)
print(energy_sum)