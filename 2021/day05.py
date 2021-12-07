from collections import defaultdict

def draw(canvas, lines):
    for [x0, y0], [x1, y1] in lines:
        xi = 1 if x1 > x0 else (-1 if x0 > x1 else 0)
        yi = 1 if y1 > y0 else (-1 if y0 > y1 else 0)
        x0, y0 = x0 - xi, y0 - yi

        while (x0, y0) != (x1, y1):
            x0, y0 = x0 + xi, y0 + yi
            canvas[(x0, y0)] += 1

    return canvas

parse_line = lambda ln: [list(map(int, c.split(','))) for c in ln.split(' -> ')]
is_orthogonal = lambda ln: ln[0][0] == ln[1][0] or ln[0][1] == ln[1][1]
is_diagonal = lambda ln: abs(ln[0][0] - ln[1][0]) == abs(ln[0][1] - ln[1][1])
count_overlaps = lambda ps: sum(1 for coord in ps if ps[coord] > 1)
lines = list(map(parse_line, open("input/day05", "r").read().strip().split('\n')))
canvas = draw(defaultdict(int), list(filter(is_orthogonal, lines)))

print("Part 1:", count_overlaps(canvas))
print("Part 2:", count_overlaps(draw(canvas, filter(is_diagonal, lines))))
