import sys

sys.path.insert(0, "../")
from utilities import success, get_input

elves = set()

proposition_directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
proposition_index = 0

for y, row in enumerate(get_input()):
    for x, char in enumerate(row):
        if char == "#":
            elves.add((x, y))


def adjacent_elves(x, y):
    total = 0
    for dx, dy in proposition_directions + [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        if (x + dx, y + dy) in elves:
            total += 1

    return total

def get_proposition(x, y, others):
    for i in range(len(proposition_directions)):
        (dx, dy) = proposition_directions[(i + proposition_index) % len(proposition_directions)]

        for i in range(-1, 2):
            nx, ny = x + (i if dx == 0 else dx), y + (i if dy == 0 else dy)

            if (nx, ny) in others:
                break
        else:
            return x + dx, y + dy

    # if there are elves everywhere, don't move
    return (x, y)


for _ in range(10):
    do_nothing = []
    move = []

    for elf in elves:
        if adjacent_elves(*elf) == 0:
            do_nothing.append(elf)
        else:
            move.append(elf)

    propositions = {}
    for elf in move:
        p = get_proposition(*elf, elves)

        if p not in propositions:
            propositions[p] = []

        propositions[p].append(elf)

    new_elves = do_nothing
    for p in propositions:
        if len(propositions[p]) != 1:
            new_elves += propositions[p]
        else:
            new_elves.append(p)

    elves = set(new_elves)
    proposition_index += 1

min_x = min(elves, key=lambda x: x[0])[0]
min_y = min(elves, key=lambda x: x[1])[1]
max_x = max(elves, key=lambda x: x[0])[0]
max_y = max(elves, key=lambda x: x[1])[1]

success((max_x - min_x + 1) * (max_y - min_y + 1) - len(elves))
