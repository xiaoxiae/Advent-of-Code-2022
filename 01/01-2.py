import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input(whole=True)

groups = []
for group in input.split("\n\n"):
    groups.append(sum(map(int, group.splitlines())))

success(sum(sorted(groups)[-3:]))
