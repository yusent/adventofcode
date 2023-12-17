def tilt(direction):
    if direction == 'north':
        for x in range(w):
            for y in range(1, h):
                while platform[y][x] == 'O' and y > 0 and platform[y-1][x] == '.':
                    platform[y][x], platform[y-1][x] = '.', 'O'
                    y -= 1
    elif direction == 'west':
        for y in range(h):
            for x in range(1, w):
                while platform[y][x] == 'O' and x > 0 and platform[y][x-1] == '.':
                    platform[y][x], platform[y][x-1] = '.', 'O'
                    x -= 1
    elif direction == 'south':
        for x in range(w):
            for y in range(h-2, -1, -1):
                while platform[y][x] == 'O' and y < h-1 and platform[y+1][x] == '.':
                    platform[y][x], platform[y+1][x] = '.', 'O'
                    y += 1
    elif direction == 'east':
        for y in range(h):
            for x in range(w-2, -1, -1):
                while platform[y][x] == 'O' and x < w-1 and platform[y][x+1] == '.':
                    platform[y][x], platform[y][x+1] = '.', 'O'
                    x += 1

def total_load():
    return sum(platform[y].count('O') * (h - y) for y in range(h))

def find_pattern_and_load(total_cycles, answered_part_1=False):
    states = {}

    for cycles in range(total_cycles):
        state = tuple(tuple(row) for row in platform)

        if state in states:
            cycle_length = cycles - states[state]
            remaining_cycles = (total_cycles - cycles) % cycle_length
            return find_pattern_and_load(remaining_cycles, True)

        states[state] = cycles

        for direction in ['north', 'west', 'south', 'east']:
            tilt(direction)

            if not answered_part_1:
                print('Part 1:', total_load())
                answered_part_1 = True

    return total_load()

platform = [list(line) for line in open('input/day14').read().splitlines()]
w, h = len(platform[0]), len(platform)
print('Part 2:', find_pattern_and_load(1_000_000_000))
