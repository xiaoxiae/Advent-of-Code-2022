import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from typing import *

pairs = get_input(whole=True).split("\n\n")

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

total = 0
for i, pair in enumerate(pairs):
    a, b = pair.splitlines()
    a = eval(a)
    b = eval(b)

    if compare(a, b) == -1:
        total += i + 1
        print(i + 1)

success(total)
