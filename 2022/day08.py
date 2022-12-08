grid = open('input/day08').read().strip().split('\n')
visibles_count = max_score = 0

def count_visible_trees_from(i, j, y_range, x_range):
    trees = 0
    for ii in y_range:
        for jj in x_range:
            trees += 1
            if grid[ii][jj] >= grid[i][j]: return trees, False
    return trees, True

for i in range(len(grid)):
    for j in range(len(grid[i])):
        left, l_visible = count_visible_trees_from(i, j, range(i, i + 1), range(j - 1, -1, -1))
        right, r_visible = count_visible_trees_from(i, j, range(i, i + 1), range(j + 1, len(grid[i])))
        up, u_visible = count_visible_trees_from(i, j, range(i - 1, -1, -1), range(j, j + 1))
        down, d_visible = count_visible_trees_from(i, j, range(i + 1, len(grid)), range(j, j + 1))
        max_score = max(max_score, left * right * up * down)
        if l_visible or r_visible or u_visible or d_visible: visibles_count += 1

print('Part 1:', visibles_count)
print('Part 2:', max_score)
