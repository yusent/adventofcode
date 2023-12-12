def sum_distances(expansion_rate):
    result = 0

    for i, (x0, y0) in enumerate(galaxies):
        for x1, y1 in galaxies[i:]:
            dx, dy = x1 - x0, y1 - y0

            if dx != 0:
                empty_cols_in_between = sum(1 for x in range(x0, x1, dx // abs(dx)) if x in empty_cols)
                result += abs(dx) - empty_cols_in_between + empty_cols_in_between * expansion_rate

            if dy != 0:
                empty_rows_in_between = sum(1 for y in range(y0, y1, dy // abs(dy)) if y in empty_rows)
                result += abs(dy) - empty_rows_in_between + empty_rows_in_between * expansion_rate

    return result

image = open('input/day11').read().splitlines()
empty_rows = [i for i in range(len(image)) if all(c == '.' for c in image[i])]
empty_cols = [i for i in range(len(image[0])) if all(image[j][i] == '.' for j in range(len(image)))]
galaxies = [(x, y) for x in range(len(image[0])) for y in range(len(image)) if image[y][x] == '#']

print('Part 1:', sum_distances(2))
print('Part 2:', sum_distances(1_000_000))
