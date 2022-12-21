import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from collections import deque


valves = {}


for row in get_input():
    parts = row.split(maxsplit=9)

    valve = parts[1]
    flow = int(parts[4][5:-1])
    leads_to = parts[-1].split(", ")

    valves[valve] = (flow, leads_to)


# precompute where we can go next from a given valve
# this removes "uninteresting" moves
valve_paths = {}
for valve in valves:
    # run BFS
    visited = set()
    queue = [(valve, 0)]
    valve_paths[valve] = {}

    while len(queue) != 0:
        current, distance = queue.pop(0)
        valve_paths[valve][current] = distance

        for neighbour in valves[current][1]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, distance + 1))

    del valve_paths[valve][valve]


queue = deque([(30, "AA", tuple(), 0)])
max_pressure = 0

while len(queue) != 0:
    remaining, current, opened, pressure = queue.popleft()

    max_pressure = max(max_pressure, pressure)

    # try to open unopened valves
    for tunnel in valve_paths[current]:
        # open only unopened and with non-0 flow
        if tunnel not in opened and valves[tunnel][0] != 0:
            distance = valve_paths[current][tunnel]
            new_opened = tuple(sorted(list(opened) + [tunnel]))

            if remaining - distance - 1 >= 0:
                queue.append(
                    (remaining - distance - 1,
                     tunnel,
                     new_opened,
                     pressure + (remaining - distance - 1) * valves[tunnel][0])
                )

success(max_pressure)
