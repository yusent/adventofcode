from re import MULTILINE, findall
from functools import cache

scanned = findall(r'^\S+ (\w+).*=(\d+).*valves? (.*)$', open('input/day16').read(), MULTILINE)
valves = { name: (int(rate), connections.split(', ')) for name, rate, connections in scanned }

@cache
def most_pressure(curr, minutes_left, closed, part2=False):
    if minutes_left <= 0: return 0

    rate, connected = valves[curr]
    pressure = (minutes_left - 1) * rate
    max_pressure = most_pressure('AA', 26, closed, False) if part2 else 0

    for valve in connected:
        max_pressure = max(
            max_pressure,
            most_pressure(valve, minutes_left - 1, closed, part2),
            pressure + most_pressure(valve, minutes_left - 2, closed - {curr}, part2) if curr in closed else 0
        )

    return max_pressure

print('Part 1:', most_pressure('AA', 30, frozenset(v for v in valves if valves[v][0] > 0)))
print('Part 2:', most_pressure('AA', 26, frozenset(v for v in valves if valves[v][0] > 0), True))
