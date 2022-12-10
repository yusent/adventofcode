p1_visited = set([(0, 0)])
p2_visited = set([(0, 0)])
rope = [(0, 0) for _ in range(10)]

DELTAS = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0),
}

def move_knot(i, dx, dy):
    rope[i] = (rope[i][0] + dx, rope[i][1] + dy)
    if i == 9: return

    next_dx = rope[i][0] - rope[i+1][0]
    next_dy = rope[i][1] - rope[i+1][1]

    if abs(next_dx) > 1 or abs(next_dy) > 1:
        move_knot(
            i + 1,
            0 if next_dx == 0 else next_dx / abs(next_dx),
            0 if next_dy == 0 else next_dy / abs(next_dy),
        )

for line in open('input/day09').read().splitlines():
    d, c = line.split()
    dx, dy = DELTAS[d]

    for _ in range(int(c)):
        move_knot(0, dx, dy)
        p1_visited.add(rope[1])
        p2_visited.add(rope[9])

print('Part 1:', len(p1_visited))
print('Part 2:', len(p2_visited))
