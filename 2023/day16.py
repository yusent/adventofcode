def next_step(y, x, direction):
    dy, dx = DIR_VECTORS[direction]
    return y + dy, x + dx, direction

def count_energized_tiles(start_y, start_x, start_direction):
    positions = [(start_y, start_x, start_direction)]
    visited_positions = set()
    visited_with_direction = set()

    while positions:
        new_positions = []

        for (y, x, direction) in positions:
            if 0 <= y < H and 0 <= x < W:
                visited_positions.add((y, x))
                if (y, x, direction) in visited_with_direction: continue
                visited_with_direction.add((y, x, direction))

                cell = GRID[y][x]

                if cell == '.':
                    new_positions.append(next_step(y, x, direction))
                elif cell == '/':
                    new_direction = {'up': 'right', 'right': 'up', 'down': 'left', 'left': 'down'}[direction]
                    new_positions.append(next_step(y, x, new_direction))
                elif cell == '\\':
                    new_direction = {'up': 'left', 'right': 'down', 'down': 'right', 'left': 'up'}[direction]
                    new_positions.append(next_step(y, x, new_direction))
                elif cell in '|-':
                    if cell == '|' and direction in ['up', 'down'] or cell == '-' and direction in ['right', 'left']:
                        new_positions.append(next_step(y, x, direction))
                        continue

                    for new_direction in ['up', 'down'] if cell == '|' else ['right', 'left']:
                        new_positions.append(next_step(y, x, new_direction))

        positions = new_positions

    return len(visited_positions)

def max_energized_tiles_count():
    mx = 0

    for y in range(H):
        mx = max(mx, count_energized_tiles(y, 0, 'right'), count_energized_tiles(y, W - 1, 'left'))

    for x in range(W):
        mx = max(mx, count_energized_tiles(0, x, 'down'), count_energized_tiles(H - 1, x, 'up'))

    return mx

GRID = open('input/day16').read().splitlines()
H, W = len(GRID), len(GRID[0])
DIR_VECTORS = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}

print('Part 1:', count_energized_tiles(0, 0, 'right'))
print('Part 2:', max_energized_tiles_count())
