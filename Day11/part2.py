image = []
horizontal = []
vertical = []
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        image.append([c for c in line])
        if all([c == "." for c in line]):
            horizontal.append(len(image) - 1)
for i in range(len(image[0])):
    if all([line[i] == "." for line in image]):
        vertical.append(i)

galaxies = []
for y in range(len(image)):
    for x in range(len(image[y])):
        if image[y][x] == "#":
            galaxies.append((x, y))

n = 1000000
sum = 0
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        minx = min(galaxies[i][0], galaxies[j][0])
        maxx = max(galaxies[i][0], galaxies[j][0])
        miny = min(galaxies[i][1], galaxies[j][1])
        maxy = max(galaxies[i][1], galaxies[j][1])
        for x in range(minx, maxx):
            if x in vertical:
                sum += n - 1
        for y in range(miny, maxy):
            if y in horizontal:
                sum += n - 1
print(sum)