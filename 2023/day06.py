from math import ceil, floor, sqrt, prod
import re

def number_of_ways_to_win(race):
    time, distance = race
    min_pressing_time_to_win = ceil((time - sqrt(time**2 - 4*distance)) / 2)
    max_pressing_time_to_win = floor((time + sqrt(time**2 - 4*distance)) / 2)
    return max_pressing_time_to_win - min_pressing_time_to_win + 1

parse_line = lambda line: [int(x) for x in line.split()[1:]]
lines = open('input/day06').readlines()
races = list(zip(*map(parse_line, lines)))

print('Part 1:', prod(number_of_ways_to_win(r) for r in races))
print('Part 2:', number_of_ways_to_win((int(re.sub(r'\D', '', line)) for line in lines)))
