import re

possigle_game_ids_sum = set_powers_sum = 0
get_max = lambda color: max(map(int, re.findall(f'(\d+) {color}', game)))

for game in open('input/day02', 'r').read().strip().split('\n'):
    r, g, b = map(get_max, ['red', 'green', 'blue'])
    set_powers_sum += r * g * b

    if r <= 12 and g <= 13 and b <= 14:
        possigle_game_ids_sum += int(game.split(': ')[0][5:])

print('Part 1: ', possigle_game_ids_sum)
print('Part 2: ', set_powers_sum)
