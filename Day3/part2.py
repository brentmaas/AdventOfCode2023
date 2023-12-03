schematic = []
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        schematic.append(line)

sum = 0
for y in range(len(schematic)):
    for x in range(len(schematic[0])):
        if schematic[y][x] == "*":
            part_number_starts = []
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if not (dx == 0 and dy == 0) and x + dx >= 0 and x + dx < len(schematic[0]) and y + dy >= 0 and y + dy < len(schematic) and schematic[y+dy][x+dx].isdigit():
                        sx = x + dx
                        sy = y + dy
                        while sx > 0 and schematic[sy][sx-1].isdigit():
                            sx -= 1
                        if not (sx, sy) in part_number_starts:
                            part_number_starts.append((sx, sy))
            if len(part_number_starts) == 2:
                mult = 1
                for px, py in part_number_starts:
                    part_number = int(schematic[py][px])
                    while px < len(schematic[0]) - 1 and schematic[py][px+1].isdigit():
                        px += 1
                        part_number = part_number * 10 + int(schematic[py][px])
                    mult *= part_number
                sum += mult
print(sum)