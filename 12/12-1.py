import sys

sys.path.insert(0, "../")
from utilities import success, get_input

scan = get_input()

def at(x, y):
    val = 'a' if scan[y][x] == 'S' else 'z' if scan[y][x] == 'E' else scan[y][x]
    return ord(val) - 97

def is_valid(x, y):
    return 0 <= x < len(scan[0]) and 0 <= y < len(scan)

def neighbours(x, y):
    n = []
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy

        if is_valid(nx, ny) and at(x, y) + 1 >= at(nx, ny):
            n.append((nx, ny))
    return n

for y in range(len(scan)):
    for x in range(len(scan[0])):
        if scan[y][x] == "S":
            start = (x, y)
        if scan[y][x] == "E":
            end = (x, y)

queue = [start]
visited = {start: 0}

while len(queue) != 0:
    current = queue.pop(0)

    for neighbour in neighbours(*current):
        if neighbour not in visited:
            visited[neighbour] = visited[current] + 1
            queue.append(neighbour)

success(visited[end])
