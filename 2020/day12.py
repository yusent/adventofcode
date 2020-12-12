from functools import reduce

def move1(pos, dir_idx, cmd, arg):
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    off_x, off_y = dirs[dir_idx]

    return {
        "N": ((pos[0], pos[1] + arg), dir_idx),
        "S": ((pos[0], pos[1] - arg), dir_idx),
        "E": ((pos[0] + arg, pos[1]), dir_idx),
        "W": ((pos[0] - arg, pos[1]), dir_idx),
        "L": (pos, ((arg // 90) * 3 + dir_idx) % 4),
        "R": (pos, (arg // 90 + dir_idx) % 4),
        "F": ((pos[0] + off_x * arg, pos[1] + off_y * arg), dir_idx),
    }[cmd]

def move2(pos, waypoint, cmd, arg):
    return {
        "N": (pos, (waypoint[0], waypoint[1] + arg)),
        "S": (pos, (waypoint[0], waypoint[1] - arg)),
        "E": (pos, (waypoint[0] + arg, waypoint[1])),
        "W": (pos, (waypoint[0] - arg, waypoint[1])),
        "L": (pos, reduce(rotate_left, range(arg // 90), waypoint)),
        "R": (pos, reduce(rotate_right, range(arg // 90), waypoint)),
        "F": ((pos[0] + waypoint[0] * arg, pos[1] + waypoint[1] * arg), waypoint),
    }[cmd]

def rotate_left(waypoint, _):
    return (-waypoint[1], waypoint[0])

def rotate_right(waypoint, _):
    return (waypoint[1], -waypoint[0])

if __name__ == "__main__":
    pos1 = (0, 0)
    pos2 = (0, 0)
    dir_idx = 0
    waypoint = (10, 1)

    for line in open("input/day12", "r").read().split():
        cmd = line[0]
        arg = int(line[1:])
        pos1, dir_idx = move1(pos1, dir_idx, cmd, arg)
        pos2, waypoint = move2(pos2, waypoint, cmd, arg)

    print(abs(pos1[0]) + abs(pos1[1]))
    print(abs(pos2[0]) + abs(pos2[1]))
