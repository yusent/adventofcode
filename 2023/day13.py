def summarize(pattern, expected_smudges=0):
    rows = pattern.splitlines()
    height = len(rows)
    width = len(rows[0])
    summary = 0

    for x in range(width-1):
        smudges = 0
        for dx in range(min(x+1, width-x-1)):
            left, right = x - dx, x + 1 + dx
            for y in range(height):
                if rows[y][left] != rows[y][right]:
                    smudges += 1
        if smudges == expected_smudges:
            summary += x + 1

    for y in range(height-1):
        smudges = 0
        for dy in range(min(y+1, height-y-1)):
            up, down = y - dy, y + 1 + dy
            for x in range(width):
                if rows[up][x] != rows[down][x]:
                    smudges += 1
        if smudges == expected_smudges:
            summary += 100 * (y + 1)

    return summary

patterns = open('input/day13').read().strip().split('\n\n')
print('Part 1:', sum(map(summarize, patterns)))
print('Part 2:', sum(summarize(p, expected_smudges=1) for p in patterns))
