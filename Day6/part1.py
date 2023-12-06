with open("Input.txt", "r") as f:
    times = [int(i) for i in f.readline().strip().split()[1:]]
    distances = [int(i) for i in f.readline().strip().split()[1:]]

mult = 1
for time, distance in zip(times, distances):
    wins = 0
    for t in range(time):
        if t * (time - t) > distance:
            wins += 1
    mult *= wins
print(mult)