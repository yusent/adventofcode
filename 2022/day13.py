from functools import cmp_to_key

def cmp(p, q):
    if p == q: return 0
    match (p, q):
        case (int(), int()): return p - q
        case ([], _): return -1
        case (_, []): return 1
        case ([x, *p], [y, *q]) if x == y: return cmp(p, q)
        case ([x, *p], [y, *q]): return cmp(x, y)
        case (int(), _): return cmp([p], q)
        case (_, int()): return cmp(p, [q])

pairs = [[eval(ln) for ln in s.split()] for s in open('input/day13').read().strip().split('\n\n')]
packets = [[[2]], [[6]], *[p for pair in pairs for p in pair]]
sorted_packets = sorted(packets, key=cmp_to_key(cmp))

print('Part 1:', sum(i for i, [p, q] in enumerate(pairs, 1) if cmp(p, q) < 0))
print('Part 2:', (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))
