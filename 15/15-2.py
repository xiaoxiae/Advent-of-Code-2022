import sys

sys.path.insert(0, "../")
from utilities import success, get_input


beacons = []
sensors = []

def d(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_bordering_values(beacon, sensor):
    """Get the bordering values of the sensor (one _after_ its range)."""
    dist = d(beacon, sensor) + 1

    values = []
    for i in range(-dist, 0 + 1):
        values.append((sensor[0] - dist + i, sensor[1] + i))
        values.append((sensor[0] - dist + i, sensor[1] - i))

    for i in range(0, dist + 1):
        values.append((sensor[0] + i, sensor[1] + dist - i))
        values.append((sensor[0] + i, sensor[1] - dist + i))

    return values

def is_covered(point, beacons, sensors):
    """Is a point covered by any of the sensors?"""
    for beacon, sensor in zip(beacons, sensors):
        if d(point, sensor) <= d(beacon, sensor):
            return True
    return False

for row in get_input():
    parts = row.split()

    sensors.append((int(parts[2][2:-1]), int(parts[3][2:-1])))
    beacons.append((int(parts[-2][2:-1]), int(parts[-1][2:])))

n = len(sensors)
max_values = 4000000

for i in range(n):
    for value in get_bordering_values(beacons[i], sensors[i]):
        if not (0 <= value[0] <= max_values and 0 <= value[1] <= max_values):
            continue

        if not is_covered(value, beacons, sensors):
            success(value[0] * 4000000 + value[1])
