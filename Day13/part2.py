sum = 0
with open("Input.txt", "r") as f:
    while True:
        terrain = []
        while (line := f.readline()).strip():
            terrain.append(line.strip())
        
        done = False
        for i in range(len(terrain[0]) - 1):
            mismatch = 0
            for j in range(min(i + 1, len(terrain[0]) - i - 1)):
                col1 = [row[i-j] for row in terrain]
                col2 = [row[i+j+1] for row in terrain]
                for k in range(len(col1)):
                    if col1[k] != col2[k]:
                        mismatch += 1
            if mismatch == 1:
                done = True
                sum += i + 1
            if done:
                break
        
        done = False
        for i in range(len(terrain) - 1):
            mismatch = 0
            for j in range(min(i + 1, len(terrain) - i - 1)):
                for k in range(len(terrain[0])):
                    if terrain[i-j][k] != terrain[i+j+1][k]:
                        mismatch += 1
            if mismatch == 1:
                done = True
                sum += 100 * (i + 1)
            if done:
                break
        
        if not line:
            break
print(sum)