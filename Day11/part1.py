image = []
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        for _ in range(2 if all([c == "." for c in line]) else 1):
            image.append([c for c in line])
i = 0
while i < len(image[0]):
    if all([line[i] == "." for line in image]):
        for j in range(len(image)):
            image[j].insert(i + 1, ".")
        i += 1
    i += 1

galaxies = []
for y in range(len(image)):
    for x in range(len(image[y])):
        if image[y][x] == "#":
            galaxies.append((x, y))

sum = 0
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
print(sum)