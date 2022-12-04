import sys

sys.path.insert(0, "../")
from utilities import success, get_input

total = 0

for line in get_input():
    a, b = line.split(",")
    a_s, a_e = map(int, a.split("-"))
    b_s, b_e = map(int, b.split("-"))

    if a_s <= b_s <= a_e or b_s <= a_s <= b_e:
        total += 1

success(total)
