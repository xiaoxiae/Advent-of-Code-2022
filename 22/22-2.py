import sys

sys.path.insert(0, "../")
from utilities import success, get_input

import re

deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
deltas_diagonal = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

field, instructions = get_input(whole=True).split("\n\n")
instructions = instructions.strip()
field = field.splitlines()

# ensure that all lines have the same length
width = max([len(l) for l in field])
for i in range(len(field)):
    field[i] = field[i].ljust(width)
height = len(field)

side_length = int((width * height // 12) ** (1/2))

# find the initial position and orientation
orientation = 0  # 0..3
x_start, y_start = 0, 0
for i, char in enumerate(field[0]):
    if char != " ":
        x_start = i
        break

# parse the instructions
moves = [int(i) for i in re.split("R|L", instructions)]
turns = re.split("\d+", instructions)[1:-1]

# find the points on the border of the field
queue = [(x_start, y_start)]
field_points = set(queue)
while len(queue) != 0:
    cx, cy = queue.pop(0)

    for dx, dy in deltas:
        nx, ny = cx + dx, cy + dy

        if not (0 <= nx < width and 0 <= ny < height):
            continue

        if field[ny][nx] == " ":
            continue

        if (nx, ny) not in field_points:
            field_points.add((nx, ny))
            queue.append((nx, ny))

# filter inner points
border_points = set()
for (cx, cy) in field_points:
    neighbouring = 0
    for dx, dy in deltas:
        nx, ny = cx + dx, cy + dy

        if (nx, ny) in field_points:
            neighbouring += 1

    if neighbouring != 4:
        border_points.add((cx, cy))


# order them by their adjacency
queue = [(cx, cy)]
sorted_border_points = []
while len(queue) != 0:
    cx, cy = queue.pop(0)
    sorted_border_points.append((cx, cy))

    for dx, dy in deltas + deltas_diagonal:
        nx, ny = cx + dx, cy + dy

        if (nx, ny) in border_points and (nx, ny) not in sorted_border_points:
            queue.append((nx, ny))
            break

border = []
for (cx, cy) in sorted_border_points:
    for o, (dx, dy) in enumerate(deltas):
        nx, ny = cx + dx, cy + dy

        if not (0 <= nx < width and 0 <= ny < height) or field[ny][nx] == " ":
            border.append((cx, cy, o))
            continue

# fix incorrectly oriented corners
for i in range(-3, len(border)):
    o1, o2, o3, o4 = [border[i+j][2] for j in range(-3, 1)]
    if o1 == o3 and o2 == o4 and o1 != o2 != o3 != o4:
        border[i + -2], border[i + -1] = border[i + -1], border[i + -2]


def is_edge_point(x, y):
    air_count = 0
    wall_count = 0
    d = None
    for i, (dx, dy) in enumerate(deltas_diagonal):
        if field[y + dy][x + dx] == " ":
            air_count += 1
            d = (dx, dy)

    for dx, dy in deltas:
        if field[y + dy][x + dx] != " ":
            wall_count += 1

    if air_count == 1 and wall_count == 4:
        return d


# portal for (x, y, orientation) returns new (x, y, orientation)
portals = {}

# create edge point portals
corner = []
for y in range(1, height - 1):
    for x in range(1, width - 1):
        d = is_edge_point(x, y)

        if d:
            a_side = []
            b_side = []
            for i in range(1, side_length + 1):
                a_in = (x + (d[0] * i), y, deltas.index((0, d[1])))
                b_in = (x, y + (d[1] * i), deltas.index((d[0], 0)))

                a_out = (b_in[0], b_in[1], (b_in[2] + 2) % len(deltas))
                b_out = (a_in[0], a_in[1], (a_in[2] + 2) % len(deltas))

                portals[a_in] = a_out
                portals[b_in] = b_out

                a_side.append(a_in)
                b_side.append(b_in)

            corner.append((a_side, b_side))

def move_and_wrap(x, y, orientation):
    if (x, y, orientation) in portals:
        return portals[(x, y, orientation)]

    dx, dy = deltas[orientation]
    nx, ny = x + dx, y + dy

    # if out of bounds, don't move there
    if (nx, ny) not in field_points:
        nx, ny = x, y

    return nx, ny, orientation

def move_forward(x, y, orientation, distance):
    if distance == 0:
        return

    for _ in range(distance):
        nx, ny, norientation = move_and_wrap(x, y, orientation)

        # if we hit a wall, simply return the previous position
        if field[ny][nx] != ".":
            return x, y, orientation

        x, y, orientation = nx, ny, norientation

    return x, y, orientation

def rotate(orientation, where):
    return (orientation + (1 if where == "R" else -1)) % len(deltas)

# walk from each side of the corner and whenever you end up, those two points wrap
for a_side, b_side in corner:
    for a, b in zip(a_side, b_side):
        for _ in range(side_length * 4):
            a = move_and_wrap(*a)
            b = move_and_wrap(*b)

        portals[a] = (b[0], b[1], (b[2] + 2) % len(deltas))
        portals[b] = (a[0], a[1], (a[2] + 2) % len(deltas))

# add the one remaining side
remaining = []
for i, b in enumerate(border):
    if b not in portals:
        remaining.append(i)

for j in range(2):
    for i in range(side_length):
        i += j * side_length * 2
        o1 = border[remaining[i]]
        o2 = border[remaining[side_length * 2 - i - 1]]

        portals[o1] = (o2[0], o2[1], (o2[2] + 2) % len(deltas))
        portals[o2] = (o1[0], o1[1], (o1[2] + 2) % len(deltas))

x, y = x_start, y_start
for i in range(len(moves)):
    x, y, orientation = move_forward(x, y, orientation, moves[i])

    if i < len(turns):
        orientation = rotate(orientation, turns[i])

success(1000 * (y + 1) + 4 * (x + 1) + orientation)
