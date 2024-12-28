from collections import deque

def get_deltas(direction):
    match direction:
        case '^': return 0, -1
        case 'v': return 0, 1
        case '<': return -1, 0
        case '>': return 1, 0

def move_p1(walls, boxes, robot_x, robot_y, dx, dy):
    x, y = robot_x, robot_y

    while True:
        x += dx
        y += dy
        if (x, y) in walls: break
        if (x, y) in boxes: continue

        robot_x += dx
        robot_y += dy

        if (robot_x, robot_y) in boxes:
            boxes.remove((robot_x, robot_y))
            boxes.add((x, y))

        break

    return robot_x, robot_y

def move_p2(walls, boxes, robot_x, robot_y, dx, dy):
    q = deque()

    if dx:
        x = robot_x

        while True:
            x += dx
            if (x, robot_y) in walls: return robot_x, robot_y

            px = x if dx == 1 else x - 1

            if (px, robot_y) in boxes:
                q.append((px, robot_y))
                x += dx
            else:
                break

    if dy:
        to_check = [(robot_x, robot_y + dy)]

        while True:
            if any((x, y) in walls for x, y in to_check): return robot_x, robot_y
            if all((x, y) not in boxes and (x - 1, y) not in boxes for x, y in to_check): break

            new_to_check = []

            for x, y in to_check:
                if (x, y) in boxes:
                    q.append((x, y))
                    new_to_check.append((x, y + dy))
                    new_to_check.append((x + 1, y + dy))

                if (x - 1, y) in boxes:
                    q.append((x - 1, y))
                    new_to_check.append((x - 1, y + dy))
                    new_to_check.append((x, y + dy))

            to_check = new_to_check

    while q:
        x, y = q.pop()
        if (x, y) not in boxes: continue

        boxes.remove((x, y))
        boxes.add((x + dx, y + dy))

    return robot_x + dx, robot_y + dy

warehouse_map, directions = open('input/day15').read().strip().split('\n\n')
deltas = list(map(get_deltas, directions.replace('\n', '')))
walls, boxes, walls_p2, boxes_p2 = set(), set(), set(), set()

for y, line in enumerate(warehouse_map.splitlines()):
    for x, cell in enumerate(line):
        match cell:
            case '#':
                walls.add((x, y))
                walls_p2.add((x * 2, y))
                walls_p2.add((x * 2 + 1, y))
            case 'O':
                boxes.add((x, y))
                boxes_p2.add((x * 2, y))
            case '@':
                robot = (x, y)
                robot_p2 = (x * 2, y)

for dx, dy in deltas:
    robot = move_p1(walls, boxes, *robot, dx, dy)
    robot_p2 = move_p2(walls_p2, boxes_p2, *robot_p2, dx, dy)

print('Part 1:', sum(x + 100 * y for x, y in boxes))
print('Part 2:', sum(x + 100 * y for x, y in boxes_p2))
