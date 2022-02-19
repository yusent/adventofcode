def parse_input():
    for section in open('input/day17').read().strip().split(','):
        start, end = section.split('=')[1].split('..')
        yield (int(start), int(end))

def gen_positions(x, y, dx, dy):
    while True:
        x += dx
        y += dy
        dx = 0 if dx == 0 else dx - 1
        dy -= 1
        yield (x, y)

if __name__ == '__main__':
    (tx0, tx1), (ty0, ty1) = parse_input()
    count = 0
    max_dy = 0

    for dx in range(1, tx1 + 1):
        for dy in range(ty0, abs(ty0)):
            for (x, y) in gen_positions(0, 0, dx, dy):
                if tx0 <= x <= tx1 and ty0 <= y <= ty1:
                    count += 1
                    max_dy = max(dy, max_dy)
                    break
                if x > tx1 or y < ty0:
                    break

    print('Part 1:', max_dy * (max_dy + 1) // 2)
    print('Part 2:', count)
