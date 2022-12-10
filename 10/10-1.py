import sys

sys.path.insert(0, "../")
from utilities import success, get_input

cycles = [20, 60, 100, 140, 180, 220]
strength = 0
X = 1

instructions = ["noop"]  # for 1-based indexing
for instruction in get_input():
    parts = instruction.split()
    if parts[0] == "addx":
        parts[0] = "noop"
    instructions += parts

for cycle, instruction in enumerate(instructions):
    if cycle in cycles:
        strength += cycle * X
        print(X, cycle * X)

    if instruction != "noop":
        X += int(instruction)

success(strength)
