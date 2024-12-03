from re import findall

def sum_products_v1(mem):
    return sum(int(a) * int(b) for a, b in findall(r'mul\((\d{1,3}),(\d{1,3})\)', mem))

def sum_products_v2(mem, disabled=False):
    result = 0
    blocks = mem.split('do()' if disabled else "don't()", maxsplit=1)

    if not disabled:
        result += sum_products_v1(blocks[0])

    if len(blocks) > 1:
        result += sum_products_v2(blocks[1], not disabled)

    return result

corrupted_mem = open('input/day03', 'r').read()
print('Part 1:', sum_products_v1(corrupted_mem))
print('Part 2:', sum_products_v2(corrupted_mem))
