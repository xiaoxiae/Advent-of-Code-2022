import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from typing import *

pairs = get_input(whole=True).split("\n\n") + ["[[2]]\n[[6]]"]

def compare(a, b) -> int:
    if len(a) == 0 and len(b) == 0:
        return 0
    if len(a) == 0:
        return -1
    if len(b) == 0:
        return 1

    u = a[0]
    v = b[0]

    if isinstance(u, int) and isinstance(v, int):
        result = -1 if u < v else 1 if u > v else 0

    elif isinstance(u, list) and isinstance(v, list):
        result = compare(u, v)

    elif isinstance(u, int) and isinstance(v, list):
        result = compare([u], v)

    elif isinstance(u, list) and isinstance(v, int):
        result = compare(u, [v])

    if result != 0:
        return result

    return compare(a[1:], b[1:])

packets = []
for pair in pairs:
    a, b = pair.splitlines()
    packets.append(eval(a))
    packets.append(eval(b))

n = len(packets)
for i in range(n):
    for j in range(i, n):
        if compare(packets[i], packets[j]) == 1:
            packets[i], packets[j] = packets[j], packets[i]

success((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
