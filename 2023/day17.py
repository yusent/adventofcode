from collections import defaultdict
from heapq import heappop, heappush

def min_heat_loss():
    heat_map = {(i, j): heat for i, line in enumerate(MAP) for j, heat in enumerate(line)}
    start_state = ((0, 0), (0, 0))
    heat_loss_map = defaultdict(lambda: float('inf'), {start_state: 0})
    q = [(0, start_state)]

    while q:
        _, current = heappop(q)
        current_pos, current_run = current

        if any(abs(n) > 3 for n in current_run): continue
        if current_pos == (H-1, W-1): return heat_loss_map[current]

        for next_state in adj_states(current_pos, current_run, 3):
            next_pos, _ = next_state
            if next_pos not in heat_map: continue

            new_heat_loss = heat_loss_map[current] + heat_map[next_pos]

            if new_heat_loss < heat_loss_map[next_state]:
                heat_loss_map[next_state] = new_heat_loss
                heappush(q, (new_heat_loss, next_state))

def adj_states(position, direction, max_run):
    y, x = position
    run_x, run_y = direction
    if run_x == 0:
        yield (y - 1, x), (-1, 0)
        yield (y + 1, x), (1, 0)
    if run_y == 0:
        yield (y, x - 1), (0, -1)
        yield (y, x + 1), (0, 1)
    if 0 < run_x < max_run:
        yield (y + 1, x), (run_x + 1, 0)
    if -max_run < run_x < 0:
        yield (y - 1, x), (run_x - 1, 0)
    if 0 < run_y < max_run:
        yield (y, x + 1), (0, run_y + 1)
    if -max_run < run_y < 0:
        yield (y, x - 1), (0, run_y - 1)

def get_direction_deltas(run_x, run_y):
    deltas = []
    if run_x == 0: deltas.extend([(-1, 0), (1, 0)])
    if run_y == 0: deltas.extend([(0, -1), (0, 1)])
    if 0 < run_x < 3: deltas.append((1, 0))
    if run_x < 0: deltas.append((-1, 0))
    if 0 < run_y < 3: deltas.append((0, 1))
    if run_y < 0: deltas.append((0, -1))
    return deltas

def ultra_min_heat_loss():
    min_run_length, max_run_length = 4, 10
    heat_costs = {(0, 0, 0, 0):0}
    completed_states = set()
    pending_states = {(0, 0, 0, 0)}

    while pending_states:
        current_state = min(pending_states, key=heat_costs.get)
        pending_states.remove(current_state)
        completed_states.add(current_state)

        x, y, prev_dx, prev_dy = current_state
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if is_reverse_direction(dx, dy, prev_dx, prev_dy):
                continue

            for step in range(min_run_length, max_run_length + 1):
                new_x, new_y = x + dx * step, y + dy * step
                if not (0 <= new_x < W and 0 <= new_y < H):
                    continue
                if (new_x, new_y, dx, dy) in completed_states:
                    continue

                new_cost = calculate_new_cost(x, y, dx, dy, step, heat_costs[current_state])
                update_heat_cost(new_x, new_y, dx, dy, new_cost, heat_costs, pending_states)

    return min(heat_costs[(x, y, dx, dy)] for x, y, dx, dy in heat_costs if x == W-1 and y == H-1)

def is_reverse_direction(dx, dy, prev_dx, prev_dy):
    return dx == prev_dx and dy == prev_dy or dx == -prev_dx and dy == -prev_dy

def calculate_new_cost(x, y, dx, dy, step, current_cost):
    new_cost = current_cost
    for i in range(1, step+1):
        new_cost += MAP[y + dy * i][x + dx * i]
    return new_cost

def update_heat_cost(x, y, dx, dy, new_cost, heat_costs, pending_states):
    if (x, y, dx, dy) not in heat_costs or heat_costs[(x, y, dx, dy)] > new_cost:
        heat_costs[(x, y, dx, dy)] = new_cost
        pending_states.add((x, y, dx, dy))

MAP = [[int(n) for n in line] for line in open('input/day17').read().splitlines()]
H = len(MAP)
W = len(MAP[0])

print('Part 1:', min_heat_loss())
print('Part 2:', ultra_min_heat_loss())
