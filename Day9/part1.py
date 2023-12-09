import numpy as np

sum = 0
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        numbers = np.array([int(i) for i in line.split(" ")])
        while not np.all(numbers == 0):
            sum += numbers[-1]
            numbers = numbers[1:] - numbers[:-1]
print(sum)