def get_delta(guard_arrow):
    match guard_arrow:
        case '^': return 0, -1
        case 'v': return 0, 1
        case '<': return -1, 0
        case '>': return 1, 0

def rotate_right(dx, dy):
    match dx, dy:
        case 0, -1: return 1, 0
        case 1, 0: return 0, 1
        case 0, 1: return -1, 0
        case -1, 0: return 0, -1

def initial_guard_position(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell not in '.#':
                return x, y, *get_delta(cell)

def visited_positions(x, y, dx, dy, grid):
    visited = set()

    while True:
        visited.add((x, y))
        new_x, new_y = x + dx, y + dy

        if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[new_y]):
            break

        if grid[new_y][new_x] == '#':
            dx, dy = rotate_right(dx, dy)
            continue

        x, y = new_x, new_y

    return visited

def in_a_loop(x, y, dx, dy, grid):
    visited = set()

    while True:
        if (x, y, dx, dy) in visited:
            return True

        visited.add((x, y, dx, dy))
        new_x, new_y = x + dx, y + dy

        if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[new_y]):
            return False

        if grid[new_y][new_x] == '#':
            dx, dy = rotate_right(dx, dy)
            continue

        x, y = new_x, new_y

def count_possible_obstacles(x, y, dx, dy, visited):
    count = 0

    for vx, vy in visited:
        if x == vx and y == vy:
            continue

        grid[vy][vx] = '#'
        count += in_a_loop(x, y, dx, dy, grid)
        grid[vy][vx] = '.'

    return count

grid = [list(line) for line in open('input/day06', 'r').read().splitlines()]
x, y, dx, dy = initial_guard_position(grid)
visited = visited_positions(x, y, dx, dy, grid)

print('Part 1:', len(visited))
print('Part 2:', count_possible_obstacles(x, y, dx, dy, visited))
