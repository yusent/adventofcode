def fold(graph, axis, value):
    g = {}

    for x, y in graph:
        index_to_change = 0 if axis == "x" else 1

        if (x, y)[index_to_change] < value:
            g[(x, y)] = True
        else:
            g[(2 * value - x, y) if axis == "x" else (x, 2 * value - y)] = True

    return g

if __name__ == "__main__":
    sections = open("input/day13", "r").read().strip().split("\n\n")
    graph = {}

    for line in sections[0].split("\n"):
        x, y = [int(v) for v in line.split(",")]
        graph[(x, y)] = True

    for i, line in enumerate(sections[1].split("\n")):
        axis, value = line.split()[-1].split("=")
        graph = fold(graph, axis, int(value))

        if i == 0:
            print("Part 1:", len(graph))

    mx = max(x for x, _ in graph.keys())
    my = max(y for _, y in graph.keys())

    print("Part 2:")
    for y in range(my + 1):
        print("".join(["#" if (x, y) in graph else " " for x in range(mx + 1)]))
