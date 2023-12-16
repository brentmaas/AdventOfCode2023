sum = 0
with open("Input.txt", "r") as f:
    while True:
        terrain = []
        while (line := f.readline()).strip():
            terrain.append(line.strip())
        
        done = False
        for i in range(len(terrain[0]) - 1):
            invalid = False
            for j in range(min(i + 1, len(terrain[0]) - i - 1)):
                if not [row[i-j] for row in terrain] == [row[i+j+1] for row in terrain]:
                    invalid = True
                    break
            if not invalid:
                done = True
                sum += i + 1
            if done:
                break
        
        done = False
        for i in range(len(terrain) - 1):
            invalid = False
            for j in range(min(i + 1, len(terrain) - i - 1)):
                if not terrain[i-j] == terrain[i+j+1]:
                    invalid = True
                    break
            if not invalid:
                done = True
                sum += 100 * (i + 1)
            if done:
                break
        
        if not line:
            break
print(sum)