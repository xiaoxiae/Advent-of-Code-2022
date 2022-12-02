import sys

sys.path.insert(0, "../")
from utilities import success, get_input


value = {"R": 1, "P": 2, "S": 3}
outcome = {"X": -1, "Y": 0, "Z": 1}
mapping = {"A": "R", "B": "P", "C": "S"}

win = {"R": "P", "P": "S", "S": "R"}
lose = {"R": "S", "P": "R", "S": "P"}

input = map(lambda x: x.split(), get_input())

total = 0
for (a, o) in input:
    a = mapping[a]
    o = outcome[o]
    rps = a if o == 0 else lose[a] if o == -1 else win[a]

    total += value[rps] + (o + 1) * 3

success(total)
