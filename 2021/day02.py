def exec(commands, part2=False):
    state = { 'h': 0, 'd': 0, 'a': 0 }
    run = run2 if part2 else run1

    for command in commands:
        direction, x = command.split(' ')
        run(state, direction, int(x))

    return state['h'] * state['d']

def run1(state, direction, x):
    if direction == 'forward':
        state['h'] += x
    elif direction == 'down':
        state['d'] += x
    else:
        state['d'] -= x

def run2(state, direction, x):
    if direction == 'forward':
        state['h'] += x
        state['d'] += state['a'] * x
    elif direction == 'down':
        state['a'] += x
    else:
        state['a'] -= x

if __name__ == "__main__":
    commands = open("input/day02", "r").read().strip().split('\n')
    print("Part 1:", exec(commands))
    print("Part 2:", exec(commands, True))
