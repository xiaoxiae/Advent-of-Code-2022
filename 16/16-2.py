import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from itertools import combinations
from collections import deque

def subsets(s):
    """Not really since we're excluding empty set and s."""
    for k in range(1, len(s)):
        for combination in combinations(s, r=k):
            yield set(combination)


valves = {}


for row in get_input():
    parts = row.split(maxsplit=9)

    valve = parts[1]
    flow = int(parts[4][5:-1])
    leads_to = parts[-1].split(", ")

    valves[valve] = (flow, leads_to)


# precompute where we can go next from a given valve (only interesting valves)
non_zero_valves = sorted([valve for valve in valves if valves[valve][0] != 0])

valve_paths = {}
for valve in non_zero_valves + ["AA"]:
    # run BFS
    visited = set()
    queue = deque([(valve, 0)])
    valve_paths[valve] = {}

    while len(queue) != 0:
        current, distance = queue.popleft()

        if current in non_zero_valves:
            valve_paths[valve][current] = distance

        for neighbour in valves[current][1]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, distance + 1))

    if valve != "AA":
        del valve_paths[valve][valve]


subset_score = {}

for subset in subsets(non_zero_valves):
    visited = {}
    queue = deque([(26, "AA", set(), 0)])

    max_pressure = 0

    while len(queue) != 0:
        remaining, current, opened, pressure = queue.popleft()

        max_pressure = max(max_pressure, pressure)

        # try to open unopened valves and in the current subset
        for tunnel in valve_paths[current]:
            if tunnel not in subset:
                continue

            if tunnel in opened:
                continue

            distance = valve_paths[current][tunnel]

            if remaining - distance - 1 < 0:
                continue

            new_opened = opened | set([tunnel])

            state = (
                (remaining - distance - 1,
                 tunnel,
                 new_opened,
                 pressure + (remaining - distance - 1) * valves[tunnel][0])
            )

            queue.append(state)

    subset_score[tuple(sorted(list(subset)))] = max_pressure


max_pressure = 0
for subset in subsets(non_zero_valves):
    key = tuple(sorted(list(subset)))
    other_key = tuple(sorted(list(set(non_zero_valves) - subset)))

    max_pressure = max(max_pressure, subset_score[key] + subset_score[other_key])


success(max_pressure)
