from collections import defaultdict, deque
from itertools import repeat

def play(cups, part2):
    cups = deque(cups + (list(range(max(cups)+1, 1000000+1)) if part2 else []))
    after = defaultdict(list)
    max_ = max(cups)

    def get_next():
        elem = cups.popleft()
        if elem in after:
            cups.extendleft(after[elem][::-1])
            del after[elem]
        return elem

    for _ in repeat(None, 10_000_000 if part2 else 100):
        current_cup = get_next()
        picked = [get_next(), get_next(), get_next()]

        destination = current_cup
        while destination in [current_cup, *picked]:
            destination = max_ if destination <= 1 else destination - 1

        after[destination] += picked
        cups.append(current_cup)

    if part2:
        while (elem := get_next()) != 1:
            cups.append(elem)

        return get_next() * get_next()
    else:
        first_part = None
        last_part = ''

        for _ in repeat(None, max_):
            elem = get_next()
            if first_part is None:
                last_part += str(elem)
                if elem == 1:
                    first_part = ''
            else:
                first_part += str(elem)

        return first_part + last_part

if __name__ == '__main__':
    cups = [6, 2, 4, 3, 9, 7, 1, 5, 8]
    print('Part 1:', play(cups, part2 = False))
    print('Part 2:', play(cups, part2 = True))
