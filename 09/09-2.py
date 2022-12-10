import sys

sys.path.insert(0, "../")
from utilities import success, get_input


def distance(head, tail):
    return max(abs(head[0] - tail[0]), abs(head[1] - tail[1]))

def move_towards(a, b):
    return 1 if a < b else 0 if a == b else -1

def move_tail(head, tail):
    """Moves the tail (if it's too far away)."""
    if distance(head, tail) > 1:
        for i in range(2):
            tail[i] += move_towards(tail[i], head[i])

visited = set([(0, 0)])
deltas = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
tails = [[0, 0] for _ in range(10)]

for instruction in get_input():
    parts = instruction.split()

    dx, dy = deltas[parts[0]]
    count = int(parts[1])

    for _ in range(count):
        tails[0][0] += dx
        tails[0][1] += dy

        for i in range(len(tails) - 1):
            move_tail(tails[i], tails[i + 1])

        visited.add(tuple(tails[-1]))

success(len(visited))
