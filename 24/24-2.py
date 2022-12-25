import sys

sys.path.insert(0, "../")
from utilities import success, get_input

import heapq


deltas = [(0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)]
blizzard_directions = "v^<>"

raw_map = get_input()
width, height = len(raw_map[0]), len(raw_map)

blizzards = []
for y, row in enumerate(raw_map):
    for x, char in enumerate(row):
        if char not in blizzard_directions:
            continue

        blizzards.append(((x, y), deltas[blizzard_directions.index(char)]))

start = (1, 0)
end = (width - 2, height - 1)


def is_valid(state):
    """Return True if the given coordinate is within bounds and not in a blizzard."""
    (x, y), steps, _ = state

    if not (0 <= x < width and 0 <= y < height):
        return False

    if raw_map[y][x] == "#":
        return False

    for (bx, by), (dx, dy) in blizzards:
        # move blizzard
        bx += dx * steps
        by += dy * steps

        # loop it around
        bx = (bx - 1) % (width - 2) + 1
        by = (by - 1) % (height - 2) + 1

        if (bx, by) == (x, y):
            return False

    return True

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(state):
    """Return the distance of a state from the end."""
    pos, steps, phase = state

    if phase == 0:
        return 2 * distance(start, end) + distance(pos, end) + steps
    elif phase == 1:
        return distance(start, end) + distance(pos, start) + steps
    elif phase == 2:
        return distance(pos, end) + steps


start_state = (start, 0, 0)

queue = [(heuristic(start_state), start_state)]
visited = set(queue)

while len(queue) != 0:
    d, ((x, y), steps, phase) = heapq.heappop(queue)

    if (x, y) == end and phase == 0:
        phase += 1
    elif (x, y) == start and phase == 1:
        phase += 1
    elif (x, y) == end and phase == 2:
        success(steps)

    for dx, dy in deltas:
        state = (x + dx, y + dy), steps + 1, phase

        if state in visited:
            continue

        if is_valid(state):
            heapq.heappush(queue, (heuristic(state), state))
            visited.add(state)

