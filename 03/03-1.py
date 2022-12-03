import sys

sys.path.insert(0, "../")
from utilities import success, get_input

total = 0

for line in get_input():
    a, b = line[len(line) // 2:], line[:len(line) // 2]

    c = list(set(a).intersection(set(b)))[0]
    total += (ord(c) - 97 + 1) if c == c.lower() else (ord(c) - 65 + 27)

success(total)
