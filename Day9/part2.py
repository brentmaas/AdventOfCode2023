import numpy as np

sum = 0
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        numbers = np.array([int(i) for i in line.split(" ")])
        historical_numbers = np.zeros([], dtype=int)
        while not np.all(numbers == 0):
            historical_numbers = np.append(historical_numbers, numbers[0])
            numbers = numbers[1:] - numbers[:-1]
        subsum = 0
        for i in range(len(historical_numbers)):
            subsum = historical_numbers[-i] - subsum
        sum += subsum
print(sum)