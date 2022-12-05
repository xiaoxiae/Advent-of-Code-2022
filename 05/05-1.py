import sys

sys.path.insert(0, "../")
from utilities import success, get_input

crates_str, commands_str = get_input(whole=True).split("\n\n")
crates_rows = crates_str.splitlines()

stacks = [[] for _ in range(int(crates_rows[-1].split()[-1]))]

for row in reversed(crates_rows[:-1]):
    for i in range(len(stacks)):
        index = 4 * i + 1
        char = row[index]

        if char != " ":
            stacks[i].append(char)

for command in commands_str.splitlines():
    parts = command.split()

    count, i_from, i_to = int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1

    for _ in range(count):
        stacks[i_to].append(stacks[i_from].pop())

success("".join(stack[-1] for stack in stacks))
