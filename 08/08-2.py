import sys

sys.path.insert(0, "../")
from utilities import success, get_input

trees = [
    list(map(lambda x: int(x), row))
    for row in get_input()
]

w, h = len(trees[0]), len(trees)

def is_valid(x, y):
    return 0 <= x < w and 0 <= y < h

max_scenic_score = 0

for y in range(h):
    for x in range(w):
        visible = []

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            visible.append(0)
            nx, ny = x, y

            while True:
                nx += dx
                ny += dy

                if not is_valid(nx, ny):
                    break

                visible[-1] += 1

                if trees[y][x] <= trees[ny][nx]:
                    break

        total = 1
        for v in visible:
            total *= v

        max_scenic_score = max(max_scenic_score, total)

success(max_scenic_score)
