with open("Input.txt", "r") as f:
    time = int("".join(f.readline().strip().split()[1:]))
    distance = int("".join(f.readline().strip().split()[1:]))

left = (0, time // 2)
while left[1] - left[0] > 1:
    new_left = (left[0] + left[1]) // 2
    if time * new_left - new_left ** 2 > distance:
        left = (left[0], new_left)
    else:
        left = (new_left, left[1])

right = (time // 2, time)
while right[1] - right[0] > 1:
    new_right = (right[0] + right[1]) // 2
    if time * new_right - new_right ** 2 > distance:
        right = (new_right, right[1])
    else:
        right = (right[0], new_right)

print(right[0] - left[0])