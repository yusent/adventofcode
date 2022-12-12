from collections import deque

def char_value(char):
    if char == 'S': char = 'a'
    if char == 'E': char = 'z'
    return ord(char)

def min_steps(part2=False):
    q = deque()
    visited = set()

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S' or part2 and cell == 'a':
                q.append((i, j, 0))

    while q:
        i, j, steps = q.popleft()
        if (i, j) in visited: continue
        if grid[i][j] == 'E': return steps
        visited.add((i, j))
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            y, x = i + di, j + dj
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and heights[y][x] <= 1 + heights[i][j]:
                q.append((y, x, steps + 1))

grid = open('input/day12').read().splitlines()
heights = [[char_value(c) for c in row] for row in grid]

print('Part 1:', min_steps())
print('Part 2:', min_steps(part2=True))
