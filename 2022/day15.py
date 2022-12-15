import re

sensors = set()

def part1():
    p1_row_y = 2_000_000
    row_beacons = set()
    neg = set()

    for line in open('input/day15').read().splitlines():
        sx, sy, bx, by = [int(p) for p in re.findall(r'-?\d+', line)]
        d = abs(sx - bx) + abs(sy - by)
        sensors.add((sx, sy, d))
        min_x = sx - d + abs(p1_row_y - sy)
        max_x = sx + d - abs(p1_row_y - sy)
        neg = neg.union(set(range(min_x, max_x + 1)))
        if by == p1_row_y: row_beacons.add(bx)

    return len(neg - row_beacons)

def part2():
    max_limit = 4_000_000
    can_be_beacon = lambda x, y: all(abs(x - sx) + abs(y - sy) > d for sx, sy, d in sensors)

    for sx, sy, d in sensors:
        for dx in range(-d - 1, d + 2):
            diff = d + 1 - abs(dx)
            for dy in [-diff, diff]:
                x = sx + dx
                y = sy + dy
                if not (0 <= x <= max_limit and 0 <= y <= max_limit): continue
                if can_be_beacon(x, y): return x * max_limit + y

print('Part 1:', part1())
print('Part 2:', part2())
