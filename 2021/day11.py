def flash(x, y, grid):
    count = 1
    grid[y][x] = -1

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if 0 <= x+i < 10 and 0 <= y+j < 10 and grid[y+j][x+i] != -1:
                grid[y+j][x+i] += 1

                if grid[y+j][x+i] > 9:
                    count += flash(x+i, y+j, grid)

    return count

def generations(grid):
    flash_count = 0
    all_flashed = False
    generation = 0

    while not all_flashed:
        generation += 1

        for x in range(10):
            for y in range(10):
                grid[y][x] += 1

        for x in range(10):
            for y in range(10):
                if grid[y][x] > 9:
                    flash_count += flash(x, y, grid)

        all_flashed = True

        for x in range(10):
            for y in range(10):
                if grid[y][x] == -1:
                    grid[y][x] = 0
                else:
                    all_flashed = False

        yield generation if all_flashed else flash_count

    return flash_count

if __name__ == "__main__":
    lines = open("input/day11", "r").read().strip().split('\n')
    grid = [[int(c) for c in line] for line in lines]
    gens = list(generations(grid))

    print("Part 1:", gens[99])
    print("Part 2:", gens[-1])
