import sys

sys.path.insert(0, "../")
from utilities import success, get_input

# shapes in relative coordinates
# (such that (0, 0) is two units from left wall) and three up from the highest rock
shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 1), (2, 1), (1, 2), (1, 0)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
]

rocks = set()
pushes = get_input(whole=True).strip()
shape_offset = [2, 3]
shape_index = 0
push_index = 0


def max_y():
    return max(rocks or [(0, 0)], key=lambda x: x[1])[1]

def shape_coordinates():
    for dx, dy in shapes[shape_index]:
        yield dx + shape_offset[0], dy + shape_offset[1]

def pprint():
    for y in reversed(range(max_y() + 10)):
        for x in range(7):
            print("@" if (x, y) in list(shape_coordinates()) else "." if (x, y) not in rocks else "#", end="")
        print()
    print()

def is_shape_valid():
    for x, y in shape_coordinates():
        if not (0 <= x < 7 and 0 <= y):
            return False

        if (x, y) in rocks:
            return False

    return True

def add_shape():
    for x, y in shape_coordinates():
        rocks.add((x, y))

def attempt_push(push):
    dx, dy = push

    shape_offset[0] += dx
    shape_offset[1] += dy

    if not is_shape_valid():
        shape_offset[0] -= dx
        shape_offset[1] -= dy

        return False

    return True


rock_count = 0
while True:
    attempt_push((-1 if pushes[push_index] == "<" else 1, 0))

    push_index = (push_index + 1) % len(pushes)

    if not attempt_push((0, -1)):
        add_shape()

        rock_count += 1
        shape_index = (shape_index + 1) % len(shapes)
        shape_offset = [2, max_y() + 4]

    if rock_count == 2022:
        break

success(shape_offset[1] - 3)
