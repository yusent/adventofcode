from collections import deque
from re import findall

def max_geodes(ore_cost, clay_cost, obs_cost_ore, obs_cost_clay, geode_cost_ore, geode_cost_obs, mins_left):
    most_geodes = 0
    q = deque([(0, 0, 0, 0, 1, 0, 0, 0, mins_left)])
    seen = set()

    while q:
        ore, clay, obs, geodes, r0, r1, r2, r3, t = q.pop()
        most_geodes = max(most_geodes, geodes)
        if t == 0: continue

        mx_ore = max(ore_cost, clay_cost, obs_cost_ore, geode_cost_ore)
        r0 = min(r0, mx_ore)
        r1 = min(r1, obs_cost_clay)
        r2 = min(r2, geode_cost_obs)
        ore = min(ore, t * mx_ore - r0 * (t-1))
        clay = min(clay, t * obs_cost_clay - r1 * (t-1))
        obs = min(obs, t * geode_cost_obs - r2 * (t-1))

        if (ore, clay, obs, geodes, r0, r1, r2, r3, t) in seen: continue
        seen.add((ore, clay, obs, geodes, r0, r1, r2, r3, t))

        q.append((ore+r0, clay+r1, obs+r2, geodes+r3, r0, r1, r2, r3, t-1))
        if ore >= ore_cost:
            q.append((ore-ore_cost+r0, clay+r1, obs+r2, geodes+r3, r0+1, r1, r2, r3, t-1))
        if ore >= clay_cost:
            q.append((ore-clay_cost+r0, clay+r1, obs+r2, geodes+r3, r0, r1+1, r2, r3, t-1))
        if ore >= obs_cost_ore and clay >= obs_cost_clay:
            q.append((ore-obs_cost_ore+r0, clay-obs_cost_clay+r1, obs+r2, geodes+r3, r0, r1, r2+1, r3, t-1))
        if ore >= geode_cost_ore and obs >= geode_cost_obs:
            q.append((ore-geode_cost_ore+r0, clay+r1, obs-geode_cost_obs+r2, geodes+r3, r0, r1, r2, r3+1, t-1))

    return most_geodes

s, p = 0, 1
for i, line in enumerate(open('input/day19').read().splitlines()):
    blueprint = tuple(map(int, findall(r'\d+', line)))
    bid, ore_cost, clay_cost, obs_cost_ore, obs_cost_clay, geode_cost_ore, geode_cost_obs = blueprint
    s += bid * max_geodes(ore_cost, clay_cost, obs_cost_ore, obs_cost_clay, geode_cost_ore, geode_cost_obs, 24)
    if i < 3: p *= max_geodes(ore_cost, clay_cost, obs_cost_ore, obs_cost_clay, geode_cost_ore, geode_cost_obs, 32)

print('Part 1:', s)
print('Part 2:', p)
