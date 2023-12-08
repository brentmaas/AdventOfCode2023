with open("Input.txt", "r") as f:
    instructions = f.readline().strip()
    f.readline()
    nodes = {}
    while line := f.readline().strip():
        node, directions = line.split(" = ")
        left, right = directions.split(", ")
        nodes[node] = (left[1:], right[:-1])
steps = 0
current_node = "AAA"
while not current_node == "ZZZ":
    for d in instructions:
        if d == "L":
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        steps += 1
        if current_node == "ZZZ":
            break
print(steps)