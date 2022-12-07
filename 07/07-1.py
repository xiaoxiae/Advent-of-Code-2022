import sys

sys.path.insert(0, "../")
from utilities import success, get_input


def sum_directories(root, pos, directories):
    total = 0

    for (f, v) in root:
        if type(v) == int:
            total += v
        else:
            total += sum_directories(root[(f, v)], pos + [f], directories)

    directories[tuple(pos)] = total

    return total


pos = []
tree = {}

for command in get_input():
    parts = command.split()

    if parts[1] == "ls":
        continue

    if parts[1] == "cd":
        if parts[2] == "..":
            pos.pop()
        elif parts[2] == "/":
            pos = []
        else:
            pos.append(parts[2])

        continue

    array = tree
    for p in pos:
        for i, v in enumerate(array):
            if v[0] == p:
                array = array[v]

    if parts[0] == "dir":
        array[(parts[1], "dir")] = {}
    else:
        array[(parts[1], int(parts[0]))] = None


directories = {}
sum_directories(tree, [], directories)

total = 0
for k, v in directories.items():
    if v < 100000:
        total += v

success(total)
