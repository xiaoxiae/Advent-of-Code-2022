import sys

sys.path.insert(0, "../")
from utilities import success, get_input


operations = {}

def get_result(node):
    if isinstance(operations[node], int):
        return operations[node]

    f = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b,
    }[operations[node][1]]

    return f(get_result(operations[node][0]), get_result(operations[node][2]))


for line in get_input():
    parts = line.split()

    if len(parts) == 4:
        operations[parts[0][:-1]] = parts[1], parts[2], parts[3]
    else:
        operations[parts[0][:-1]] = int(parts[1])

print(get_result("root"))
