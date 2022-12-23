import sys

sys.path.insert(0, "../")
from utilities import success, get_input

import re

deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

field, instructions = get_input(whole=True).split("\n\n")
instructions = instructions.strip()
field = field.splitlines()

# ensure that all lines have the same length
maze_length = max([len(l) for l in field])
for i in range(len(field)):
    field[i] = field[i].ljust(maze_length)


orientation = 0  # 0..3
x, y = 0, 0
for i, char in enumerate(field[0]):
    if char != " ":
        x = i
        break

moves = [int(i) for i in re.split("R|L", instructions)]
turns = re.split("\d+", instructions)[1:-1]


def move_and_wrap(x, y, delta):
    while True:
        y = (y + delta[1]) % len(field)
        x = (x + delta[0]) % len(field[y])

        if field[y][x] != " ":
            return x, y

def move_forward(x, y, orientation, distance):
    if distance == 0:
        return

    dx, dy = deltas[orientation]

    for _ in range(distance):
        nx, ny = move_and_wrap(x, y, (dx, dy))

        # if we hit a wall, simply return the previous position
        if field[ny][nx] != ".":
            return x, y

        x, y = nx, ny

    return x, y

def rotate(orientation, where):
    return (orientation + (1 if where == "R" else -1)) % len(deltas)


for i in range(len(moves)):
    x, y = move_forward(x, y, orientation, moves[i])

    if i < len(turns):
        orientation = rotate(orientation, turns[i])

success(1000 * (y + 1) + 4 * (x + 1) + orientation)

