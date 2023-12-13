def sum_valid_cases(spring_conditions, unfold_factor=1):
    total = 0

    for line in spring_conditions:
        dots, blocks = line.split()
        dots = '?'.join([dots] * unfold_factor)
        blocks = ','.join([blocks] * unfold_factor)
        blocks = [int(x) for x in blocks.split(',')]
        MEMO.clear()
        total += count_valid_cases(dots, blocks, 0, 0, 0)

    return total

def count_valid_cases(dots, blocks, pos, block, block_size):
    key = (pos, block, block_size)
    if key in MEMO: return MEMO[key]

    if pos == len(dots):
        if block == len(blocks) and block_size == 0: return 1
        elif block == len(blocks) - 1 and blocks[block] == block_size: return 1
        else: return 0

    valid_cases = 0

    for c in ['.', '#']:
        if dots[pos] == c or dots[pos] == '?':
            if c == '.' and block_size == 0:
                valid_cases += count_valid_cases(dots, blocks, pos + 1, block, 0)
            elif c == '.' and block_size > 0 and block < len(blocks) and blocks[block] == block_size:
                valid_cases += count_valid_cases(dots, blocks, pos + 1, block + 1, 0)
            elif c == '#':
                valid_cases += count_valid_cases(dots, blocks, pos + 1, block, block_size + 1)

    MEMO[key] = valid_cases
    return valid_cases

spring_lines = open('input/day12').read().splitlines()
MEMO = {}
print("Part 1:", sum_valid_cases(spring_lines))
print("Part 2:", sum_valid_cases(spring_lines, unfold_factor=5))
