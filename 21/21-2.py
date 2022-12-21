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

lo = 1
hi = 1

operations["humn"] = 0
ineq = get_result(operations["root"][0]) < get_result(operations["root"][2])

while True:
    operations["humn"] = hi

    if ineq != (get_result(operations["root"][0]) <= get_result(operations["root"][2])):
        break

    hi *= 2

while lo < hi:
    avg = (lo + hi) // 2

    operations["humn"] = avg

    if ineq == (get_result(operations["root"][0]) <= get_result(operations["root"][2])):
        lo = avg + 1
    else:
        hi = avg

success(avg)
