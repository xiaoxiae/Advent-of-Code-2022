import sys

sys.path.insert(0, "../")
from utilities import success, get_input

total = 0

input = get_input()

for i in range(len(input) // 3):
    a = input[i * 3]
    b = input[i * 3 + 1]
    c = input[i * 3 + 2]

    char = list(set(a).intersection(set(b)).intersection(set(c)))[0]
    total += (ord(char) - 97 + 1) if char == char.lower() else (ord(char) - 65 + 27)

success(total)
