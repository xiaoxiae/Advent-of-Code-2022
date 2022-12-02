import sys

sys.path.insert(0, "../")
from utilities import success, get_input


def rps(a, b):
    return 0 if a == b else \
           -1 if (a == "R" and b == "S") \
              or (a == "S" and b == "P") \
              or (a == "P" and b == "R") \
           else 1


value = {"R": 1, "P": 2, "S": 3}
mapping = {
    "A": "R", "B": "P", "C": "S",
    "X": "R", "Y": "P", "Z": "S",
}

input = map(lambda x: x.split(), get_input())

total = 0
for (a, b) in input:
    a, b = mapping[a], mapping[b]
    total += value[b] + (rps(a, b) + 1) * 3

success(total)
