import sys

sys.path.insert(0, "../")
from utilities import success, get_input


cubes = []

for cube in get_input():
    x, y, z = map(int, cube.split(","))

    cubes.append((x, y, z))


total = 0

for (x, y, z) in cubes:
    for dx, dy, dz in [(1, 0, 0), (0, 1, 0), (0, 0, 1),
                       (-1, 0, 0), (0, -1, 0), (0, 0, -1)]:
        nx, ny, nz = x + dx, y + dy, z + dz

        if (nx, ny, nz) not in cubes:
            total += 1

success(total)

