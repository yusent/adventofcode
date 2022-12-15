from collections import defaultdict
from copy import deepcopy

class InfSet():
    def __contains__(self, item):
        return True

lines = open('input/day14').read().splitlines()
paths = [[[int(c) for c in pnt.split(',')] for pnt in ln.split(' -> ')] for ln in lines]
grid = defaultdict(set)
max_y = 0

for path in paths:
    for i in range(len(path) - 1):
        px, py = path[i]
        qx, qy = path[i+1]
        max_y = max(py, qy, max_y)
        if px == qx:
            start, end = sorted([py, qy])
            for yi in range(start, end + 1): grid[yi].add(px)
        else:
            start, end = sorted([px, qx])
            for xi in range(start, end + 1): grid[py].add(xi)

grid[max_y+2] = InfSet()

def drop_sand(grid, part1=True):
    sand_count = 0
    while True:
        sx, sy = 500, 0
        while True:
            if part1 and sy == max_y:
                return sand_count
            elif sx not in grid[sy+1]:
                sy += 1
            elif (sx - 1) not in grid[sy+1]:
                sx -= 1
                sy += 1
            elif (sx + 1) not in grid[sy+1]:
                sx += 1
                sy += 1
            else:
                sand_count += 1
                grid[sy].add(sx)
                break
        if sy == 0: return sand_count

print('Part 1:', drop_sand(deepcopy(grid)))
print('Part 2:', drop_sand(grid, False))
