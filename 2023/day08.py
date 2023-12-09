from math import lcm
from itertools import count
from functools import reduce
import re

def count_steps_to_reach_z(starting_nodes_end_with='AAA'):
    positions = [s for s in network[steps[0]] if s.endswith(starting_nodes_end_with)]
    steps_to_finish = {}

    for i in count():
        next_positions = []

        for j, pos in enumerate(positions):
            next_pos = network[steps[i % len(steps)]][pos]
            if next_pos.endswith('Z'):
                steps_to_finish[j] = i + 1
                if len(steps_to_finish) == len(positions):
                    return reduce(lcm, steps_to_finish.values())
            next_positions.append(next_pos)

        positions = next_positions

steps, instructions = open('input/day08').read().strip().split('\n\n')
network = {'L': {}, 'R': {}}

for instruction in instructions.splitlines():
    state, left, right = re.findall(r'\w+', instruction)
    network['L'][state] = left
    network['R'][state] = right

print('Part 1:', count_steps_to_reach_z())
print('Part 2:', count_steps_to_reach_z(starting_nodes_end_with='A'))
