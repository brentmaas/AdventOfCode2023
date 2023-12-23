def hash_string(string):
    val = 0
    for c in string:
        val += ord(c)
        val = (17 * val) % 256
    return val

boxes = [[] for _ in range (256)]
focal_lengths = [[] for _ in range (256)]
with open("Input.txt", "r") as f:
    for string in f.readline().strip().split(","):
        if "-" in string and (label := string[:-1]) in boxes[(hash_value := hash_string(label))]:
            focal_lengths[hash_value].pop(boxes[hash_value].index(label))
            boxes[hash_value].remove(label)
        elif "=" in string:
            label = string[:-2]
            hash_value = hash_string(label)
            focal_length = int(string[-1])
            if label in boxes[hash_value]:
                focal_lengths[hash_value][boxes[hash_value].index(label)] = focal_length
            else:
                boxes[hash_value].append(label)
                focal_lengths[hash_value].append(focal_length)

focusing_power = 0
for i in range(256):
    for j in range(len(boxes[i])):
        focusing_power += (i + 1) * (j + 1) * focal_lengths[i][j]
print(focusing_power)