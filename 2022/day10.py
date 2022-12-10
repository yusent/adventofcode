cycle = signal = 0
x = 1
screen = '\n'

def tick():
    global cycle, signal, screen
    screen += '#' if x - 1 <= cycle % 40 <= x + 1 else '.'
    cycle += 1
    if cycle % 40 == 0: screen += '\n'
    if cycle % 40 == 20: signal += cycle * x

for line in open('input/day10').read().splitlines():
    match line.split():
        case ["noop"]:
            tick()
        case ["addx", v]:
            tick()
            tick()
            x += int(v)

print('Part 1:', signal)
print('Part 2:', screen)
