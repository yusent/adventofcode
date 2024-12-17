from re import match

def parse_machine(machine_section):
    m = match(r'\D*(\d+)\D*(\d+)\n\D*(\d+)\D*(\d+)\n\D*(\d+)\D*(\d+)', machine_section)
    return (int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5]), int(m[6]))

def calc_presses(machine, offset=0):
    ax, ay, bx, by, x, y = machine
    x += offset
    y += offset

    # From the description we get 2 equations:
    # (1) a_presses * ax + b_presses * bx = x
    # (2) a_presses * ay + b_presses * by = y
    # Multiplying (1) by ay/ax gives us:
    # (3) a_presses * ay + b_presses * (bx * ay / ax) = x * ay / ax
    # Subtracting (2) from (3) gives us:
    b_presses = round((ay / ax * x - y) / (bx * ay / ax - by), 2)

    # From (1) we can now calculate a_presses:
    a_presses = round((x - b_presses * bx) / ax, 2)

    # Both a_presses and b_presses should be integers to be a valid solution
    if int(a_presses) == a_presses and int(b_presses) == b_presses:
        return (int(a_presses), int(b_presses))

machines = list(map(parse_machine, open('input/day13').read().split('\n\n')))
spent_tokens = 0
adjusted_spent_tokens = 0

for machine in machines:
    if presses := calc_presses(machine):
        spent_tokens += 3 * presses[0] + presses[1]

    if presses := calc_presses(machine, 10000000000000):
        adjusted_spent_tokens += 3 * presses[0] + presses[1]

print('Part 1:', spent_tokens)
print('Part 2:', adjusted_spent_tokens)
