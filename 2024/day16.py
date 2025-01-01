from heapq import heappush, heappop

def traverse(reverse=False):
    visited = set()
    scores = {}
    queue = [(0, 1, *START)]

    if reverse:
        queue = []

        for dir_idx in range(4):
            heappush(queue, (0, dir_idx, *END))

    while queue:
        score, dir_idx, x, y = heappop(queue)

        if (x, y, dir_idx) not in scores:
            scores[(x, y, dir_idx)] = score

        if not reverse and (x, y) == END: return score, scores
        if (x, y, dir_idx) in visited: continue

        visited.add((x, y, dir_idx))
        dx, dy = DIRS[(dir_idx + 2) % 4 if reverse else dir_idx]
        nx, ny = x + dx, y + dy

        if (nx, ny) not in WALLS:
            heappush(queue, (score + 1, dir_idx, nx, ny))

        heappush(queue, (score + 1000, (dir_idx + 1) % 4, x, y))
        heappush(queue, (score + 1000, (dir_idx + 3) % 4, x, y))

    return scores

WALLS = set()
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for i, line in enumerate(open('input/day16').read().splitlines()):
    for j, cell in enumerate(line):
        match cell:
            case '#': WALLS.add((j, i))
            case 'S': START = (j, i)
            case 'E': END = (j, i)

min_score, scores = traverse()
rev_scores = traverse(reverse=True)
good_spots = set()

for x, y, dir_idx in scores:
    if (x, y, dir_idx) in rev_scores and scores[(x, y, dir_idx)] + rev_scores[(x, y, dir_idx)] == min_score:
        good_spots.add((x, y))

print('Part 1:', min_score)
print('Part 2:', len(good_spots))
