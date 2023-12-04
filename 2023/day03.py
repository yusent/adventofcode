import math

def neighbors(y, x):
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if 0 <= y + dy < h and 0 <= x + dx < w:
                yield y + dy, x + dx

def num_end(y, x):
    end = x
    while end < w and schematic[y][end].isdigit(): end += 1
    return end

def number_on(y, x):
    if not schematic[y][x].isdigit(): return

    # Move to the start of the number
    while x > 0 and schematic[y][x - 1].isdigit():
        x -= 1

    end = num_end(y, x)
    return int(schematic[y][x:end])

schematic = open('input/day03', 'r').read().splitlines()
h, w = len(schematic), len(schematic[0])
sum_of_parts = 0
sum_of_gear_ratios = 0

for y in range(h):
    x = 0

    while x < w:
        if schematic[y][x] == '*':
            adjacent_numbers = set()

            for ny, nx in neighbors(y, x):
                number = number_on(ny, nx)
                if number:
                    adjacent_numbers.add(number)

            if len(adjacent_numbers) == 2:
                sum_of_gear_ratios += math.prod(adjacent_numbers)
        elif schematic[y][x].isdigit():
            xa, x = x, num_end(y, x)

            if any(schematic[ny][nx] not in '0123456789.' for xi in range(xa, x) for ny, nx in neighbors(y, xi)):
                sum_of_parts += int(schematic[y][xa:x])
                continue

        x += 1

print('Part 1:', sum_of_parts)
print('Part 2:', sum_of_gear_ratios)
