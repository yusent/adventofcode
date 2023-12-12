def find_start_position():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S': return x, y

def first_step_from(x, y):
    if maze[y][x+1] in '-J7':
        return x+1, y
    elif maze[y][x-1] in '-LF':
        return x-1, y
    elif maze[y+1][x] in '|LJ':
        return x, y+1
    return x, y-1

def find_inner_side(loop):
    fl_count = j7_count = dash_count = 0
    for i, (x, y) in enumerate(loop):
        if maze[y][x] == '-':
            rng = range(y-1, -1, -1) if loop[i-1][0] < x else range(y+1, len(maze))
            for j in rng:
                if (x, j) in loop:
                    if maze[j][x] == '-': dash_count += 1
                    elif maze[j][x] == 'F': fl_count += 1
                    elif maze[j][x] == 'L': fl_count -= 1
                    elif maze[j][x] == '7': j7_count += 1
                    elif maze[j][x] == 'J': j7_count -= 1
            break
    return 'left' if (dash_count + (abs(fl_count) + abs(j7_count)) // 2) % 2 == 1 else 'right'

def get_loop():
    x, y = find_start_position()
    loop = [(x, y)]
    x, y = first_step_from(x, y)
    loop.append((x, y))

    while maze[y][x] != 'S':
        prev_x, prev_y = loop[-2]
        cell = maze[y][x]

        if cell == '-' and prev_x == x-1 or cell == 'F' and prev_y > y or cell == 'L' and prev_y == y-1:
            x += 1
        elif cell == 'J' and prev_y < y or cell == '7' and prev_y == y+1 or cell == '-' and prev_x == x+1:
            x -= 1
        elif cell == 'J' and prev_x == x-1 or cell == 'L' and prev_x > x or cell == '|' and prev_y == y+1:
            y -= 1
        else:
            y += 1

        loop.append((x, y))

    return loop

def count_enclosed_tiles(loop):
    enclosed = set()
    lr = find_inner_side(loop)

    for li, (x, y) in enumerate(loop):
        prev_x, prev_y = loop[li-1]

        up = any([
            maze[y][x] == '-' and (lr == 'left' and prev_x < x or lr == 'right' and prev_x > x),
            maze[y][x] == 'F' and (lr == 'left' and prev_y > y or lr == 'right' and prev_x > x),
            maze[y][x] == '7' and (lr == 'right' and prev_y > y or lr == 'left' and prev_x < x)
        ])

        down = any([
            maze[y][x] == '-' and (lr == 'left' and prev_x > x or lr == 'right' and prev_x < x),
            maze[y][x] == 'J' and (lr == 'left' and prev_y < y or lr == 'right' and prev_x < x),
            maze[y][x] == 'L' and (lr == 'right' and prev_y < y or lr == 'left' and prev_x > x)
        ])

        left = any([
            maze[y][x] == '|' and (lr == 'left' and prev_y > y or lr == 'right' and prev_y < y),
            maze[y][x] == 'L' and (lr == 'left' and prev_x > x or lr == 'right' and prev_y < y),
            maze[y][x] == 'F' and (lr == 'right' and prev_x > x or lr == 'left' and prev_y > y)
        ])

        right = any([
            maze[y][x] == '|' and (lr == 'right' and prev_y > y or lr == 'left' and prev_y < y),
            maze[y][x] == '7' and (lr == 'left' and prev_x < x or lr == 'right' and prev_y > y),
            maze[y][x] == 'J' and (lr == 'right' and prev_x < x or lr == 'left' and prev_y < y),
        ])

        if up:
            for i in range(y-1, -1, -1):
                if (x, i) in loop: break
                enclosed.add((x, i))
        if down:
            for i in range(y+1, len(maze)):
                if (x, i) in loop: break
                enclosed.add((x, i))
        if left:
            for i in range(x-1, -1, -1):
                if (i, y) in loop: break
                enclosed.add((i, y))
        if right:
            for i in range(x+1, len(maze[y])):
                if (i, y) in loop: break
                enclosed.add((i, y))

    return len(enclosed)

maze = open('input/day10').readlines()
loop = get_loop()
print('Part 1:', len(loop) // 2)
print('Part 2:', count_enclosed_tiles(loop))
