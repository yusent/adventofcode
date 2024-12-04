def count_xmas_occurrences(word):
    return word.count('XMAS') + word.count('SAMX')

def count_grid_xmas_occurrences(grid):
    # Horizontal
    count = sum(map(count_xmas_occurrences, grid))

    # Vertical
    for j in range(len(grid[0])):
        count += count_xmas_occurrences(''.join([grid[i][j] for i in range(len(grid))]))

    # Diagonal
    for i in range(len(grid) - 3):
        for j in range(len(grid[0]) - 3):
            # Descending to the right
            count += count_xmas_occurrences(''.join([grid[i + d][j + d] for d in range(4)]))

            # Descending to the left
            count += count_xmas_occurrences(''.join([grid[i + d][j - d] for d in range(4)]))

    return count

def count_x_mas_occurrences(grid):
    count = 0

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            tl_br = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
            tr_bl = grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1]

            if (tl_br == 'SAM' or tl_br == 'MAS') and (tr_bl == 'SAM' or tr_bl == 'MAS'):
                count += 1

    return count

grid = open('input/day04', 'r').read().splitlines()
print('Part 1:', count_grid_xmas_occurrences(grid))
print('Part 2:', count_x_mas_occurrences(grid))
