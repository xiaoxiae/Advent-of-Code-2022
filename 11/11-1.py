import sys

sys.path.insert(0, "../")
from utilities import success, get_input

from dataclasses import dataclass
from typing import *

@dataclass
class Monkey:
    items: List
    operation: Callable[int, int]
    throw: Callable[int, int]

    @classmethod
    def from_string(cls, string):
        lines = string.splitlines()

        items = list(map(int, lines[1].split(maxsplit=2)[-1].split(",")))

        op, val = lines[2].split()[-2:]
        operation = lambda x: (x + int(val)) if op == "+" \
                              else (x * x) if val == "old" \
                              else (x * int(val))

        mod = int(lines[-3].split()[-1])
        if_true = int(lines[-2].split()[-1])
        if_false = int(lines[-1].split()[-1])
        throw = lambda x: if_true if x % mod == 0 else if_false

        return cls(items, operation, throw)

    def __len__(self):
        return len(self.items)

    def throw_item(self) -> Tuple[int, int]:
        """Throw an item to the monkey, returning it as a (item, monkey) tuple."""
        item = self.items.pop(0)
        item = self.operation(item)
        item //= 3

        return (item, self.throw(item))

    def catch_item(self, item: int):
        self.items.append(item)


monkeys = []
for part in get_input(whole=True).split("\n\n"):
    monkeys.append(Monkey.from_string(part))

monkey_activity = [0] * len(monkeys)
for _ in range(20):
    for i, monkey in enumerate(monkeys):
        while len(monkey) != 0:
            item, monkey_id = monkey.throw_item()
            monkey_activity[i] += 1
            monkeys[monkey_id].catch_item(item)

monkey_activity = sorted(monkey_activity)

success(monkey_activity[-1] * monkey_activity[-2])
