from functools import cache
from math import floor, log10

@cache
def count_stones(stone, blinks):
    if blinks == 0: return 1
    if stone == 0: return count_stones(1, blinks - 1)

    if (size := floor(log10(stone)) + 1) % 2 == 0:
        return sum(count_stones(st, blinks - 1) for st in divmod(stone, 10 ** (size // 2)))

    return count_stones(stone * 2024, blinks - 1)

stones = list(map(int, open('input/day11').read().split()))

print('Part 1:', sum(count_stones(stone, 25) for stone in stones))
print('Part 2:', sum(count_stones(stone, 75) for stone in stones))
