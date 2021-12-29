def move_herd(graph, height, width, down=False):
    moves = set()

    for i, j in graph:
        if not down and graph[(i, j)] == ">" and (i, (j + 1) % width) not in graph:
            moves.add(((i, j), (i, (j + 1) % width)))
        elif down and graph[(i, j)] == "v" and ((i + 1) % height, j) not in graph:
            moves.add(((i, j), ((i + 1) % height, j)))

    for src, dst in moves:
        graph[dst] = graph.pop(src)

    return len(moves) > 0

def find_stale_step(graph, height, width):
    step = 0

    while True:
        step += 1
        moved_horizontally = move_herd(graph, height, width)
        moved_vertically = move_herd(graph, height, width, True)

        if not moved_horizontally and not moved_vertically:
            break

    return step

if __name__ == "__main__":
    graph = {}
    rows = open("input/day25").read().strip().split("\n")
    height = len(rows)
    width = len(rows[0])

    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char != ".":
                graph[(i, j)] = char

    print("Part 1:", find_stale_step(graph, height, width))
