def hand_type(hand):
    decomposed_hand = {}
    jokers = 0
    for c in hand:
        if c == "J":
            jokers += 1
        else:
            if not c in decomposed_hand:
                decomposed_hand[c] = 1
            else:
                decomposed_hand[c] += 1
    values = list(decomposed_hand.values())
    max_value = 0 if len(values) == 0 else max(values)
    if max_value + jokers == 5:
        return 6
    if max_value + jokers == 4:
        return 5
    if (3 in values and 2 in values) or (values.count(2) == 2 and jokers == 1):
        return 4
    if max_value + jokers == 3:
        return 3
    if values.count(2) == 2:
        return 2
    if max_value + jokers == 2:
        return 1
    return 0

def hand_values(hand):
    values = []
    for c in hand:
        if c >= '2' and c <= '9':
            values.append(int(c))
        elif c == 'T':
            values.append(10)
        elif c == 'J':
            values.append(1)
        elif c == 'Q':
            values.append(12)
        elif c == 'K':
            values.append(13)
        elif c == 'A':
            values.append(14)
    return values

hands = []
with open("Input.txt", "r") as f:
    while line := f.readline().strip():
        hand, bid = line.split(" ")
        hands.append((hand_type(hand), hand_values(hand), int(bid)))

def compare_greater_than(left, right):
    if left[0] > right[0]:
        return True
    if left[0] < right[0]:
        return False
    for i in range(5):
        if left[1][i] > right[1][i]:
            return True
        if left[1][i] < right[1][i]:
            return False
    return False

for i in range(0, len(hands) - 1):
    for j in range(0, len(hands) - i - 1):
        if compare_greater_than(hands[j], hands[j+1]):
            hands[j], hands[j+1] = hands[j+1], hands[j]

sum = 0
for i in range(len(hands)):
    sum += hands[i][2] * (i + 1)
print(sum)