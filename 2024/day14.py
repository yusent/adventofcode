from collections import deque
from itertools import count
from re import match

def parse_robot(line):
    return tuple(map(int, match(r'\D+(\d+),(\d+) v=(.*),(.*)', line).groups()))

def safety_factor(robots):
    # q0 | q1
    # -------
    # q2 | q3
    q0 = q1 = q2 = q3 = 0
    t = 100

    for px, py, vx, vy in robots:
        x = (px + vx * t) % W
        y = (py + vy * t) % H

        if x < W // 2 and y < H // 2:
            q0 += 1
        elif x > W // 2 and y < H // 2:
            q1 += 1
        elif x < W // 2 and y > H // 2:
            q2 += 1
        elif x > W // 2 and y > H // 2:
            q3 += 1

    return q0 * q1 * q2 * q3

def run_until_easter_egg_shows(robots):
    for t in count(1):
        robot_positions = set()
        seen = set()
        max_object_size = 0

        for i, (px, py, vx, vy) in enumerate(robots):
            x = (px + vx) % W
            y = (py + vy) % H
            robots[i] = (x, y, vx, vy)
            robot_positions.add((x, y))

        for x, y in robot_positions:
            if (x, y) in seen: continue
            object_size = 0
            q = deque([(x, y)])

            while q:
                x, y = q.pop()
                if (x, y) in seen: continue

                object_size += 1
                seen.add((x, y))

                for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    if (x + dx, y + dy) in robot_positions:
                        q.append((x + dx, y + dy))

            max_object_size = max(max_object_size, object_size)

        if max_object_size > 50:
            return t

W, H = 101, 103
robots = list(map(parse_robot, open('input/day14').read().splitlines()))

print('Part 1:', safety_factor(robots))
print('Part 2:', run_until_easter_egg_shows(robots))
