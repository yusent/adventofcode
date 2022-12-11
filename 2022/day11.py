from collections import deque
from copy import deepcopy
from math import prod

def parse_monkey(section):
    lines = section.splitlines()
    return [
        deque(int(d) for d in lines[1].split(': ')[1].split(', ')),
        eval(f'lambda old:{lines[2].split("=")[1]}'),
        int(lines[3].split()[-1]),
        int(lines[4].split()[-1]),
        int(lines[5].split()[-1]),
        0 # Inspections count
    ]

def monkey_business_level(monkeys, part1=True):
    mod = prod(m[2] for m in monkeys)

    for _ in range(20 if part1 else 10_000):
        for monkey in monkeys:
            while monkey[0]:
                monkey[5] += 1
                item = monkey[1](monkey[0].popleft())
                if part1:
                    item //= 3
                else:
                    item %= mod
                monkeys[monkey[3 if item % monkey[2] == 0 else 4]][0].append(item)

    return prod(sorted(m[5] for m in monkeys)[-2:])

monkeys = [parse_monkey(section) for section in open('input/day11').read().strip().split('\n\n')]
print('Part 1:', monkey_business_level(deepcopy(monkeys)))
print('Part 2:', monkey_business_level(monkeys, part1=False))
