from math import prod

def get_basin(height_map, y, x, basin):
    p = height_map[y][x]

    if p > 8 or (x, y) in basin:
        return basin

    basin[(x, y)] = p

    for i, j in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
        basin = get_basin(height_map, j, i, basin)

    return basin

def find_basins(height_map):
    width = len(height_map[0]) + 2
    height_map = [[9] * width, *[[9, *row, 9] for row in height_map], [9] * width]
    basins = []

    for y in range(1, len(height_map) - 1):
        for x in range(1, len(height_map[y]) - 1):
            p = height_map[y][x]

            if p > 8 or any((x, y) in b for b in basins):
                continue

            basins.append(get_basin(height_map, y, x, {}))

    return basins

if __name__ == "__main__":
    lines = open("input/day09", "r").read().strip().split('\n')
    height_map = [[int(c) for c in line] for line in lines]
    basins = find_basins(height_map)

    print("Part 1:", sum(min(b.values()) + 1 for b in basins))
    print("Part 2:", prod(sorted(len(b) for b in basins)[-3:]))
