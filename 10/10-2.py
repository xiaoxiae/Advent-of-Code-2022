import sys

sys.path.insert(0, "../")
from utilities import success, get_input

crt = ""
X = 1

instructions = []
for instruction in get_input():
    parts = instruction.split()
    if parts[0] == "addx":
        parts[0] = "noop"
    instructions += parts

for cycle, instruction in enumerate(instructions):
    if cycle % 40 == 0:
        crt += "\n"

    if cycle % 40 in [X - 1, X, X + 1]:
        crt += "#"
    else:
        crt += "."

    if instruction != "noop":
        X += int(instruction)

success(crt)
