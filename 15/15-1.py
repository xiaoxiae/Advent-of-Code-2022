import sys

sys.path.insert(0, "../")
from utilities import success, get_input


beacons = []
sensors = []

def d(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_beacon_interval(beacon, sensor, y):
    """Get the interval of values at level y which is covered by the sensor."""
    dy = abs(y - sensor[1])
    dist = d(beacon, sensor)

    interval = (sensor[0] - dist + dy, sensor[0] + dist - dy)

    return None if interval[0] > interval[1] else interval

for row in get_input():
    parts = row.split()

    sensors.append((int(parts[2][2:-1]), int(parts[3][2:-1])))
    beacons.append((int(parts[-2][2:-1]), int(parts[-1][2:])))

n = len(sensors)
y = 2000000

intervals = []
for i in range(n):
    interval = get_beacon_interval(beacons[i], sensors[i], y)

    if interval is not None:
        intervals.append(interval)

# slow and disgusting but I'm too lazy
values = set()
for interval in intervals:
    values = values.union(set(range(*interval)))

success(len(values))
