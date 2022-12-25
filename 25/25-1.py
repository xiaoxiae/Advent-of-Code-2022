import sys

sys.path.insert(0, "../")
from utilities import success, get_input

def snafu_to_decimal(number):
    chars = "=-012"
    total = 0
    for i, char in enumerate(reversed(number)):
        total += (chars.index(char) - 2) * 5 ** i
    return total

def decimal_to_snafu(number):
    i = 1
    while i <= number:
        i *= 5
    i //= 5

    # get the powers of 5
    powers = []
    while i != 0:
        powers.append(number // i)
        number = number % i
        i //= 5

    while not all([-2 <= d <= 2 for d in powers]):

        i = len(powers) - 1
        while i >= 0:
            if powers[i] >= 3:
                if i == 0:
                    powers = [0] + powers
                    i += 1

                powers[i] -= 5
                powers[i - 1] += 1

            i -= 1

    return "".join(["=-012"[p + 2] for p in powers])


total = 0
for number in get_input():
    total += snafu_to_decimal(number)

success(decimal_to_snafu(total))
