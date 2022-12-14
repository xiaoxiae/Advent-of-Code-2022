import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from collections import defaultdict
from typing import *


def parse(a: str) -> Tuple[int]:
    return tuple(map(int, a.split(",")))

def sign(a: int) -> int:
    return -1 if a < 0 else 0 if a == 0 else 1

def return_points_between(a: str, b: str) -> List:
    (x1, y1), (x2, y2) = parse(a), parse(b)

    dx = sign(x2 - x1)
    dy = sign(y2 - y1)

    coords = [(x1, y1)]
    while (x1, y1) != (x2, y2):
        x1 += dx
        y1 += dy
        coords.append((x1, y1))

    return coords

def simulate_fall(cave) -> Optional[Tuple[int]]:
    s_x, s_y = (500, 0)

    while True:
        if cave[(s_x, s_y + 1)] is None:
            s_y += 1
        elif cave[(s_x - 1, s_y + 1)] is None:
            s_y += 1
            s_x -= 1
        elif cave[(s_x + 1, s_y + 1)] is None:
            s_y += 1
            s_x += 1
        else:
            return s_x, s_y

        if s_y == max_y + 1:
            return (s_x, s_y)


cave = defaultdict(lambda: None)
for line in get_input():
    coords = line.split(" -> ")

    for i in range(len(coords) - 1):
        for p in return_points_between(coords[i], coords[i + 1]):
            cave[p] = "#"

max_y = max(cave.keys(), key=lambda x: x[1])[1]

sand = 0
while True:
    s_coord = simulate_fall(cave)
    cave[s_coord] = "o"
    sand += 1

    if s_coord[1] == 0:
        break

success(sand)
