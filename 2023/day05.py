from functools import reduce

def map_value(mapping, seed):
    # Maps a single seed number through a given mapping
    for dst_start, src_start, length in mapping:
        if src_start <= seed < src_start + length:
            return seed - src_start + dst_start
    return seed

def map_range(mapping, seed_range):
    # Maps a range of seed numbers through a given mapping
    result = []
    for dst_start, src_start, length in mapping:
        src_end = src_start + length
        next_range = []
        while seed_range:
            start, end = seed_range.pop()
            if start < src_start:
                next_range.append((start, min(end, src_start)))
            if end > src_start:
                mapped_start = max(start, src_start) - src_start + dst_start
                mapped_end = min(end, src_end) - src_start + dst_start
                result.append((mapped_start, mapped_end))
            if end > src_end:
                next_range.append((max(start, src_end), end))
        seed_range = next_range
    return result + seed_range

def process_seed(seed):
    # Process a single seed through all mappings
    return reduce(lambda acc, m: map_value(m, acc), mappings, seed)

def process_seed_range(seed_range):
    # Process a range of seeds through all mappings
    start, size = seed_range
    ranges = [(start, start + size)]
    for mapping in mappings:
        ranges = map_range(mapping, ranges)
    return min(r[0] for r in ranges)

seeds, *maps = open('input/day05').read().strip().split('\n\n')
seeds = list(map(int, seeds.split(':')[1].split()))
mappings = [[tuple(map(int, line.split())) for line in section.splitlines()[1:]] for section in maps]

print('Part 1:', min(map(process_seed, seeds)))
print('Part 2:', min(process_seed_range((seeds[i], seeds[i + 1])) for i in range(0, len(seeds), 2)))
