from itertools import cycle

jet_pattern = open('input/day17').read().strip()
moves_size = len(jet_pattern)
move_dirs = cycle(jet_pattern)
hbar = lambda y: {(x, y) for x in range(2, 6)}
cross = lambda y: {(x, y+1) for x in range(2, 5)} | {(3, y+2), (3, y)}
angle = lambda y: {(x, y) for x in range(2, 5)} | {(4, y+1), (4, y+2)}
vbar = lambda y: {(2, y+dy) for dy in range(4)}
square = lambda y: {(2, y), (3, y), (2, y+1), (3, y+1)}
shapes = cycle([hbar, cross, angle, vbar, square])
tower = {(x, 0) for x in range(7)}
move_r = lambda s: {(x+1, y) for x, y in s} if all(x < 6 and (x+1, y) not in tower for x, y in s) else s
move_l = lambda s: {(x-1, y) for x, y in s} if all(x > 0 and (x-1, y) not in tower for x, y in s) else s
move = lambda shape: move_r(shape) if next(move_dirs) == '>' else move_l(shape)
sig = lambda: frozenset((x, height-y) for x, y in tower if height-y<=30)
limit = 1_000_000_000_000
patterns = {}
height = moves_index = i = offset = 0

while i < limit:
    if i == 2022: print('Part 1:', height)
    shape = next(shapes)(height + 4)
    while True:
        shape = move(shape)
        moves_index = (moves_index + 1) % moves_size
        if all((x, y-1) not in tower for x, y in shape):
            shape = {(x, y-1) for x, y in shape}
            continue
        tower |= shape
        height = max(height, *(y for x, y in shape))
        pattern = (moves_index, i % 5, sig())
        if pattern in patterns:
            prev_i, prev_height = patterns[pattern]
            reps = (limit - i) // (i - prev_i)
            offset += reps * (height - prev_height)
            i += reps * (i - prev_i)
        patterns[pattern] = (i, height)
        break
    i += 1

print('Part 2:', height + offset)
