def parse_board(section):
    rows = [list(map(int, line.split())) for line in section.split('\n')]
    cols = list(map(list, zip(*rows))) # Transpose
    return (rows, cols)

def scratch(num, rows):
    return list(map(lambda row: list(filter(lambda x: x != num, row)), rows))

if __name__ == "__main__":
    sections = open("input/day04", "r").read().strip().split('\n\n')
    boards = list(map(parse_board, sections[1:]))
    scores = []

    for num in map(int, sections[0].split(',')):
        for i in range(len(boards)):
            rows, cols = boards[i]
            rows = scratch(num, rows)
            cols = scratch(num, cols)

            if not all(rows) or not all(cols):
                scores.append(num * sum(sum(row) for row in rows))
                boards[i] = None
            else:
                boards[i] = (rows, cols)

        boards = list(filter(None, boards))

    print("Part 1:", scores[0])
    print("Part 2:", scores[-1])
