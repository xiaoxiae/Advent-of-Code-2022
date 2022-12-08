import sys

sys.path.insert(0, "../")
from utilities import success, get_input

trees = [
    list(map(lambda x: int(x), row))
    for row in get_input()
]

visible = set()

w, h = len(trees[0]), len(trees)

for y in range(h):
    for d in [range(w), reversed(range(w))]:
        highest = float('-inf')

        for x in d:
            if trees[y][x] > highest:
                visible.add((x, y))
                highest = trees[y][x]

for x in range(w):
    for d in [range(h), reversed(range(h))]:
        highest = float('-inf')

        for y in d:
            if trees[y][x] > highest:
                visible.add((x, y))
                highest = trees[y][x]

success(len(visible))
