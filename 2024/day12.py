from collections import defaultdict

VISITED = set()

def traverse(x, y, plot, borders):
    if (x, y) in VISITED: return 0, borders

    VISITED.add((x, y))
    area = 1

    for border_direction, dx, dy in [('l', -1, 0), ('r', 1, 0), ('u', 0, -1), ('d', 0, 1)]:
        if 0 <= x + dx < len(plot[y]) and 0 <= y + dy < len(plot) and plot[y + dy][x + dx] == plot[y][x]:
            area += traverse(x + dx, y + dy, plot, borders)[0]
            continue

        if border_direction in 'lr':
            borders[(border_direction, x)].add(y)
        else:
            borders[(border_direction, y)].add(x)

    return area, borders

def count_sides(borders):
    borders = sorted(borders)
    return 1 + sum(1 for i in range(1, len(borders)) if borders[i] - borders[i - 1] > 1)

plot = open('input/day12').read().splitlines()
total_price = 0
total_price_with_discount = 0

for y in range(len(plot)):
    for x in range(len(plot[y])):
        area, borders = traverse(x, y, plot, defaultdict(set))
        perimeter = sum(map(len, borders.values()))
        sides = sum(map(count_sides, borders.values()))
        total_price += area * perimeter
        total_price_with_discount += area * sides

print('Part 1:', total_price)
print('Part 2:', total_price_with_discount)
