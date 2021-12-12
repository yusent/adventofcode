from collections import defaultdict

def get_paths(graph, allow_small = True, node = "start", visited = set()):
    if node in visited:
        return []

    if node == "end":
        return ["end"]

    paths = set()
    valid_small_cave = False

    if node[0].islower():
        if allow_small and node != "start":
            valid_small_cave = True
            allow_small = False
        else:
            visited = set([*visited, node])

    for n in graph[node]:
        if valid_small_cave:
            for c in get_paths(graph, True, n, set([*visited, node])):
                paths.add(f'{node},{c}')

        for c in get_paths(graph, allow_small, n, visited):
            paths.add(f'{node},{c}')

    return paths

if __name__ == "__main__":
    lines = open("input/day12", "r").read().strip().split('\n')
    graph = defaultdict(list)

    for line in lines:
        src, dst = line.split("-")
        graph[src].append(dst)
        graph[dst].append(src)

    print("Part 1:", len(get_paths(graph, False)))
    print("Part 2:", len(get_paths(graph)))
