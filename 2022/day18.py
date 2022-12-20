from collections import deque

def parse_cube(line):
    global max_x, max_y, max_z
    x, y, z = tuple(map(int, line.split(',')))
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    max_z = max(max_z, z)
    return (x, y, z)

def exposed(x, y, z):
    global inside, outside
    if (x, y, z) in outside: return True
    if (x, y, z) in inside: return False

    visited, q = set(), deque([(x, y, z)])

    while q:
        x, y, z = q.popleft()
        if (x, y, z) in cubes or (x, y, z) in visited: continue
        visited.add((x, y, z))
        if x > max_x or y > max_y or z > max_z:
            outside |= visited
            return True
        for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            q.append((x + dx, y + dy, z + dz))

    inside |= visited
    return False

max_x = max_y = max_z = exposed_area = 0
cubes = set(map(parse_cube, open('input/day18').read().splitlines()))
inside, outside, visited = set(), set(), set()
area = len(cubes) * 6

for x, y, z in cubes:
    for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        if (x + dx, y + dy, z + dz) in cubes: area -= 1
        if exposed(x + dx, y + dy, z + dz): exposed_area += 1

print('Part 1:', area)
print('Part 2:', exposed_area)
