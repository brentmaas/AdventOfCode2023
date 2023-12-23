def hash_string(string):
    val = 0
    for c in string:
        val += ord(c)
        val = (17 * val) % 256
    return val

hash_sum = 0
with open("Input.txt", "r") as f:
    for string in f.readline().strip().split(","):
        hash_sum += hash_string(string)
print(hash_sum)