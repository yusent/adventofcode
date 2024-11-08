DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}

def hex_to_distance_and_dir(hex_code):
    direction = "RDLU"[int(hex_code[-2])]
    distance = int(hex_code[2:-2], 16)
    return direction, distance

def parse_instruction(line, part2=False):
    direction, distance, hex_code = line.split()
    return hex_to_distance_and_dir(hex_code) if part2 else (direction, int(distance))

def calculate_vertices(dig_plan, part2=False):
    vertices = [(0, 0)]
    boundary = 0

    for line in dig_plan:
        direction, distance = parse_instruction(line, part2)
        dx, dy = DIRECTIONS[direction]
        prev_x, prev_y = vertices[-1]
        vertices.append((prev_x + dx * distance, prev_y + dy * distance))
        boundary += distance

    return vertices, boundary

def calculate_area(vertices, boundary):
    xs, ys = zip(*vertices)
    left_sum = sum(x * ys[i+1] for i, x in enumerate(xs[:-1]))
    right_sum = sum(y * xs[i+1] for i, y in enumerate(ys[:-1]))
    area = abs(left_sum - right_sum) // 2
    return area + boundary // 2 + 1

dig_plan = open("input/day18").read().splitlines()
vertices_p1, boundary_p1 = calculate_vertices(dig_plan)
vertices_p2, boundary_p2 = calculate_vertices(dig_plan, part2=True)

print('Part 1:', calculate_area(vertices_p1, boundary_p1))
print('Part 2:', calculate_area(vertices_p2, boundary_p2))
