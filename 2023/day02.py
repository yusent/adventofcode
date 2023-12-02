import re

possigle_game_ids_sum = 0
set_powers_sum = 0

for game in open('input/day02', 'r').read().strip().split('\n'):
    max_red = max(int(m.split(' ')[0]) for m in re.findall(r'\d+ red', game))
    max_green = max(int(m.split(' ')[0]) for m in re.findall(r'\d+ green', game))
    max_blue = max(int(m.split(' ')[0]) for m in re.findall(r'\d+ blue', game))
    set_powers_sum += max_red * max_green * max_blue

    if max_red <= 12 and max_green <= 13 and max_blue <= 14:
        possigle_game_ids_sum += int(game.split(': ')[0][5:])

print('Part 1: ', possigle_game_ids_sum)
print('Part 2: ', set_powers_sum)
