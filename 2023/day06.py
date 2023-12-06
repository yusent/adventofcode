from functools import reduce
from math import ceil, floor, sqrt, prod

def number_of_ways_to_win(race):
    time, distance = race
    min_pressing_time_to_win = ceil((time - sqrt(time**2 - 4*distance)) / 2)
    max_pressing_time_to_win = floor((time + sqrt(time**2 - 4*distance)) / 2)
    return max_pressing_time_to_win - min_pressing_time_to_win + 1

parse_line = lambda line: [int(x) for x in line.split()[1:]]
races = list(zip(*map(parse_line, open('input/day06').readlines())))
p2_race = (int(x) for x in reduce(lambda acc, r: (acc[0]+str(r[0]), acc[1]+str(r[1])), races, ('', '')))

print('Part 1:', prod(number_of_ways_to_win(r) for r in races))
print('Part 2:', number_of_ways_to_win(p2_race))
