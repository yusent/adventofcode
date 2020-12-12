import itertools

def count(prev, rule2 = False):
    state = next_round(prev, rule2)

    if state != prev:
        return count(state, rule2)

    result = 0

    for row in state:
        for cell in row:
            if cell == "#":
                result += 1

    return result

def next_round(layout, rule2):
    result = list(map(lambda x: x[:], layout))

    for y, x in itertools.product(range(len(layout)), range(len(layout[0]))):
        neighbours_count = 0

        for off_x, off_y in itertools.product(range(-1, 2), range(-1, 2)):
            if off_x == 0 and off_y == 0:
                continue

            neighbours_count += find_seat(layout, x, y, off_x, off_y, rule2)

        if layout[y][x] == "L" and neighbours_count == 0:
            result[y][x] = "#"

        if layout[y][x] == "#" and neighbours_count >= 4 + int(rule2):
            result[y][x] = "L"

    return result

def find_seat(layout, x, y, off_x, off_y, rule2):
    cell = at(layout, x + off_x, y + off_y)

    if cell == "#":
        return 1

    if cell == "." and rule2:
        return find_seat(layout, x + off_x, y + off_y, off_x, off_y, rule2)

    return 0

def at(layout, x, y):
    if y in range(len(layout)) and x in range(len(layout[y])):
        return layout[y][x]

    return None

if __name__ == "__main__":
    file_contents = open("input/day11", "r").read()
    layout = list(map(list, file_contents.split()))

    print("Part 1:", count(layout))
    print("Part 2:", count(layout, True))
