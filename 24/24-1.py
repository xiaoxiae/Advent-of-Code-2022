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
    (x, y), steps = state

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

def heuristic(state):
    """Return the distance of a state from the end."""
    (x, y), steps = state
    return abs(x - end[0]) + abs(y - end[0]) + steps


start_state = (start, 0)

queue = [(heuristic(start_state), start_state)]
visited = set(queue)

while len(queue) != 0:
    d, ((x, y), steps) = heapq.heappop(queue)

    if (x, y) == end:
        success(steps)

    for dx, dy in deltas:
        state = (x + dx, y + dy), steps + 1

        if state in visited:
            continue

        if is_valid(state):
            heapq.heappush(queue, (heuristic(state), state))
            visited.add(state)

