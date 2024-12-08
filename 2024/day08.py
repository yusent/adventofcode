from collections import defaultdict
from itertools import count

input_lines = open('input/day08').read().splitlines()
antennas_map = defaultdict(list)
w = len(input_lines[0])
h = len(input_lines)
antinodes = set()
with_harmonics = set()

for i, line in enumerate(input_lines):
    for j, char in enumerate(line):
        if char != '.':
            antennas_map[char].append((i, j))

for locs in antennas_map.values():
    for i in range(len(locs)):
        for j in range(i + 1, len(locs)):
            a0_y = locs[i][0]
            a0_x = locs[i][1]
            a1_y = locs[j][0]
            a1_x = locs[j][1]
            dy = a1_y - a0_y
            dx = a1_x - a0_x

            for k in count():
                if a0_y < 0 or a0_y >= h or a0_x < 0 or a0_x >= w:
                    break

                if k == 1:
                    antinodes.add((a0_y, a0_x))

                with_harmonics.add((a0_y, a0_x))
                a0_y = a0_y - dy
                a0_x = a0_x - dx

            for k in count():
                if a1_y < 0 or a1_y >= h or a1_x < 0 or a1_x >= w:
                    break

                if k == 1:
                    antinodes.add((a1_y, a1_x))

                with_harmonics.add((a1_y, a1_x))
                a1_y = a1_y + dy
                a1_x = a1_x + dx

print('Part 1:', len(antinodes))
print('Part 2:', len(with_harmonics))
