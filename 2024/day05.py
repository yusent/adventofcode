from collections import defaultdict

def middle_page(update):
    return update[len(update) // 2]

rules_section, updates_section = open('input/day05', 'r').read().split('\n\n')
rules = defaultdict(set)
p1 = p2 = 0

for line in rules_section.splitlines():
    page0, page1 = line.split('|')
    rules[int(page0)].add(int(page1))

for line in updates_section.splitlines():
    update = list(map(int, line.split(',')))
    pages_before = {}
    swapped = False

    for i in range(len(update)):
        while err_pages := rules[update[i]] & pages_before.keys():
            swap_idx = min(pages_before[err_page] for err_page in err_pages)
            update[swap_idx], update[i] = update[i], update[swap_idx]
            pages_before[update[swap_idx]] = swap_idx
            swapped = True

        pages_before[update[i]] = i

    if swapped:
        p2 += middle_page(update)
    else:
        p1 += middle_page(update)

print('Part 1:', p1)
print('Part 2:', p2)
