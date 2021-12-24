from heapq import heappop, heappush

def lowest_total_rist(risk_levels, scale=1):
    height = len(risk_levels)
    width = len(risk_levels[0])
    risks = [[0] * scale * width for _ in range(scale * height)]
    queue = [(0, 0, 0)]

    while any(queue):
        (r, y, x) = heappop(queue)

        if y < 0 or y >= scale * height or x < 0 or x >= scale * width:
            continue

        val = risk_levels[y % height][x % width] + y // height + x // width
        risk = r + (val % 9 if val > 9 else val)

        if risks[y][x] > 0 and risk >= risks[y][x]:
            continue

        risks[y][x] = risk

        if y == scale * height - 1 and x == scale * width - 1:
            break

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            heappush(queue, (risks[y][x], y + dy, x + dx))

    return risks[scale * height - 1][scale * width - 1] - risk_levels[0][0]

if __name__ == "__main__":
    file_contents = open('input/day15', 'r').read().strip()
    risk_levels = [list(map(int, line)) for line in file_contents.split('\n')]
    print("Part 1:", lowest_total_rist(risk_levels))
    print("Part 2:", lowest_total_rist(risk_levels, 5))
