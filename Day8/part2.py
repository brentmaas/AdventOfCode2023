with open("Input.txt", "r") as f:
    instructions = f.readline().strip()
    f.readline()
    nodes = {}
    while line := f.readline().strip():
        node, directions = line.split(" = ")
        left, right = directions.split(", ")
        nodes[node] = (left[1:], right[:-1])

current_nodes = [node for node in list(nodes.keys()) if node.endswith("A")]
previous_nodes = [[] for _ in range(len(current_nodes))]
visited_exit = [[False] for _ in range(len(current_nodes))]
cycled = [False for _ in range(len(current_nodes))]
while not all(cycled):
    for d in instructions:
        for i in range(len(current_nodes)):
            if d == "L":
                current_nodes[i] = nodes[current_nodes[i]][0]
            else:
                current_nodes[i] = nodes[current_nodes[i]][1]
            if not cycled[i] and current_nodes[i].endswith("Z"):
                visited_exit[i][-1] = True
        if all([current_node.endswith("Z") for current_node in current_nodes]):
            break
    for i in range(len(current_nodes)):
        if not cycled[i]:
            if current_nodes[i] in previous_nodes[i]:
                cycled[i] = True
                visited_exit[i].pop(-1)
                visited_exit[i] = visited_exit[i][previous_nodes[i].index(current_nodes[i]):]
                previous_nodes[i] = previous_nodes[i][previous_nodes[i].index(current_nodes[i]):]
            else:
                previous_nodes[i].append(current_nodes[i])
                visited_exit[i].append(False)

visit_indices = []
for exits in visited_exit:
    visit_indices.append(exits.index(True))

steps = 0
base = 1
for i in range(len(visit_indices)):
    while not steps % len(visited_exit[i]) == visit_indices[i] - 1:
        steps += base
    base *= len(visited_exit[i])
steps = (steps + 1) * len(instructions)

current_nodes = [previous_nodes[i][visit_indices[i]-1] for i in range(len(previous_nodes))]
for d in instructions:
    for i in range(len(current_nodes)):
        if d == "L":
            current_nodes[i] = nodes[current_nodes[i]][0]
        else:
            current_nodes[i] = nodes[current_nodes[i]][1]
    steps += 1
    if all([current_node.endswith("Z") for current_node in current_nodes]):
        break
print(steps)