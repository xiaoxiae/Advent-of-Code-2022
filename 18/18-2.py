import sys

sys.path.insert(0, "../")
from utilities import success, get_input


cubes = set()

for cube in get_input():
    x, y, z = map(int, cube.split(","))

    cubes.add((x, y, z))

min_bounds = tuple(min(cubes, key=lambda x: x[i])[i] - 1 for i in range(3))
max_bounds = tuple(max(cubes, key=lambda x: x[i])[i] + 1 for i in range(3))

deltas = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

def in_bounds(pos):
    for i, v in enumerate(pos):
        if not min_bounds[i] <= v <= max_bounds[i]:
            return False
    return True

def neighbouring(pos):
    x, y, z = pos
    for dx, dy, dz in deltas:
        new_pos = x + dx, y + dy, z + dz

        if in_bounds(new_pos):
            yield new_pos

def touching(pos):
    count = 0
    for neighbour in neighbouring(pos):
        if neighbour in cubes:
            count += 1

    return count


# calculate areas of all of the pockets
queue = [min_bounds]
visited = set(queue)
total = 0

while len(queue) != 0:
    current = queue.pop()

    total += touching(current)

    for neighbour in neighbouring(current):
        if neighbour in cubes:
            continue

        if neighbour not in visited:
            queue.append(neighbour)
            visited.add(neighbour)

success(total)
