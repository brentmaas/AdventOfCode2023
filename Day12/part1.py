def reduce_springs(springs, arrangements):
    if len(springs) == 0:
        return [], []
    
    while len(springs) > 0 and springs[0] == ".":
        springs.pop(0)
    while len(springs) > 0 and springs[-1] == ".":
        springs.pop(-1)
    i = 1
    while i < len(springs):
        if springs[i] == "." and springs[i-1] == ".":
            springs.pop(i)
        else:
            i += 1
    
    if len(arrangements) == 0:
        return [], []
    
    min_length = sum(arrangements) + len(arrangements) - 1
    if len(springs) == min_length:
        return [], []
    
    while len(arrangements) > 0:
        start = 0
        while start < len(springs) - 1 and springs[start] != "#":
            start += 1
        end = start
        while end < len(springs) - 1 and springs[end+1] == "#":
            end += 1
        potential_end = end
        while potential_end < len(springs) - 1 and springs[potential_end+1] != ".":
            potential_end += 1
        
        if start <= arrangements[0] and springs[start] == "#":
            if end - start + 1 == arrangements[0]:
                springs = springs[end+2:]
                arrangements.pop(0)
            elif start <= potential_end and potential_end + 1 == arrangements[0]:
                springs = springs[potential_end+2:]
                arrangements.pop(0)
            elif start == 0 and potential_end + 1 >= arrangements[0]:
                springs = springs[arrangements[0]+1:]
                arrangements.pop(0)
            else:
                something_happened = False
                for i in range(start + 1, arrangements[0]):
                    if springs[i] != "#":
                        springs[i] = "#"
                        something_happened = True
                for i in range(max(0, potential_end - arrangements[0] + 1), start):
                    if springs[i] != "#":
                        springs[i] = "#"
                        something_happened = True
                if not something_happened:
                    break
        else:
            break
    while len(arrangements) > 0:
        start = len(springs) - 1
        while start > 0 and springs[start] != "#":
            start -= 1
        end = start
        while end > 0 and springs[end-1] == "#":
            end -= 1
        potential_end = end
        while potential_end > 0 and springs[potential_end-1] != ".":
            potential_end -= 1
        
        if len(springs) - start - 1 <= arrangements[-1] and springs[start] == "#":
            if start - end + 1 == arrangements[-1]:
                springs = springs[:max(0, end - 1)]
                arrangements.pop(-1)
            elif start >= potential_end and len(springs) - potential_end == arrangements[-1]:
                springs = springs[:max(0, potential_end - 1)]
                arrangements.pop(-1)
            elif start == len(springs) - 1 and len(springs) - potential_end >= arrangements[-1]:
                springs = springs[:max(0, len(springs) - arrangements[-1] - 1)]
                arrangements.pop(-1)
            else:
                something_happened = False
                for i in range(len(springs) - arrangements[-1], start):
                    if springs[i] != "#":
                        springs[i] = "#"
                        something_happened = True
                for i in range(start, min(len(springs) - 1, potential_end + arrangements[-1])):
                    if springs[i] != "#":
                        springs[i] = "#"
                        something_happened = True
                if not something_happened:
                    break
        else:
            break
    
    while len(springs) > 0 and springs[0] == ".":
        springs.pop(0)
    while len(springs) > 0 and springs[-1] == ".":
        springs.pop(-1)
    
    if len(arrangements) > 0:
        lengths = []
        starts = []
        pot_lengths = []
        pot_starts = []
        i = 0
        while i < len(springs):
            if springs[i] == "#":
                if i > 0 and springs[i-1] == "#" and len(lengths) > 0:
                    lengths[-1] += 1
                else:
                    starts.append(i)
                    lengths.append(1)
            if springs[i] != ".":
                if i > 0 and springs[i-1] != "." and len(pot_lengths) > 0:
                    pot_lengths[-1] += 1
                else:
                    pot_starts.append(i)
                    pot_lengths.append(1)
            i += 1
        
        for length in range(max(pot_lengths), -1, -1):
            num_pot_lengths = pot_lengths.count(length)
            num_lengths = lengths.count(length)
            num_arrangements = arrangements.count(length)
            if num_pot_lengths == num_arrangements:
                for start in [pot_starts[i] for i in range(len(pot_starts)) if pot_lengths[i] == length]:
                    for i in range(start, start + length):
                        springs[i] = "#"
            elif num_lengths == num_arrangements:
                for start in [starts[i] for i in range(len(starts)) if lengths[i] == length]:
                    if start > 0:
                        springs[start-1] = "."
                    if start + length < len(springs):
                        springs[start+length] = "."
                break
            else:
                break
    
    if len(arrangements) == 0:
        return [], []
    
    min_length = sum(arrangements) + len(arrangements) - 1
    if len(springs) == min_length:
        return [], []
    
    while len(springs) > 0 and springs[0] == ".":
        springs.pop(0)
    while len(springs) > 0 and springs[-1] == ".":
        springs.pop(-1)
    
    return springs, arrangements

def get_arrangements(springs):
    arrangements = []
    for i in range(len(springs)):
        if springs[i] == "#":
            if i == 0 or springs[i-1] == ".":
                arrangements.append(1)
            else:
                arrangements[-1] += 1
    return arrangements

def is_valid(springs, arrangements):
    if "?" in springs:
        return False
    return arrangements == get_arrangements(springs)

def count_arrangements(springs, arrangements):
    if len(springs) == 0:
        return 1
    arrangement_count = 0
    unknowns = [i for i in range(len(springs)) if springs[i] == "?"]
    considered = list(range(sum(arrangements) - sum([1 for c in springs if c == "#"])))
    while True:
        springs_copy = springs.copy()
        for i in range(len(unknowns)):
            springs_copy[unknowns[i]] = "#" if i in considered else "."
            if is_valid(springs_copy, arrangements):
                arrangement_count += 1
        
        to_update = len(considered) - 1
        while to_update >= 0:
            if considered[to_update] < len(unknowns) - len(considered) + to_update:
                considered[to_update] += 1
                for i in range(to_update + 1, len(considered)):
                    considered[i] = considered[i-1] + 1
                break
            else:
                to_update -= 1
        if to_update < 0:
            break
    return arrangement_count

arrangement_sum = 0
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        springs, arrangements = line.split(" ")
        springs = [c for c in springs]
        arrangements = [int(c) for c in arrangements.split(",")]
        springs, arrangements = reduce_springs(springs, arrangements)
        arrangement_sum += count_arrangements(springs, arrangements)
print(arrangement_sum)