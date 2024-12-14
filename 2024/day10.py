def traverse(_map, y, x, h=0):
    if y < 0 or y >= len(_map) or x < 0 or x >= len(_map[y]) or _map[y][x] != str(h): return set(), 0
    if _map[y][x] == '9': return {(y, x)}, 1
    reachable_9s, trails = set(), 0

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r9s, trs = traverse(_map, y + dy, x + dx, h + 1)
        reachable_9s |= r9s
        trails += trs

    return reachable_9s, trails

_map = open('input/day10').read().splitlines()
scores_sum = 0
ratings_sum = 0

for i, row in enumerate(_map):
    for j, cell in enumerate(row):
        if cell == '0':
            reachable_9s, trailhead_rating = traverse(_map, i, j)
            scores_sum += len(reachable_9s)
            ratings_sum += trailhead_rating

print('Part 1:', scores_sum)
print('Part 2:', ratings_sum)
