def exec1(commands):
    d = 0
    x = 0

    for command in commands:
        s = command.split(' ')
        direction = s[0]
        steps = int(s[1])

        if direction == 'forward':
            x += steps
        elif direction == 'down':
            d += steps
        else:
            d -= steps

    return d * x

def exec2(commands):
    d = 0
    x = 0
    aim = 0

    for command in commands:
        s = command.split(' ')
        direction = s[0]
        steps = int(s[1])

        if direction == 'forward':
            x += steps
            d += aim * steps
        elif direction == 'down':
            aim += steps
        else:
            aim -= steps

    return d * x

if __name__ == "__main__":
    commands = open("input/day02", "r").read().strip().split('\n')
    print("Part 1:", exec1(commands))
    print("Part 2:", exec2(commands))
