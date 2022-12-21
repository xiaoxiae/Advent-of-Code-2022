import sys

sys.path.insert(0, "../")
from utilities import success, get_input


numbers = [[i, int(v)] for i, v in enumerate(get_input(whole=True).split())]

def mix(i):
    for j, (k, _) in enumerate(numbers):
        if i == k:
            break

    n = numbers.pop(j)

    new_i = (j + n[1]) % len(numbers)

    if new_i == 0:
        new_i = len(numbers)
    elif new_i == len(numbers):
        new_i = 0

    numbers.insert(new_i, n)

for i in range(len(numbers)):
    mix(i)

for zero_pos, (_, n) in enumerate(numbers):
    if n == 0:
        break

success(sum([numbers[(i + zero_pos) % len(numbers)][1] for i in [1000, 2000, 3000]]))
