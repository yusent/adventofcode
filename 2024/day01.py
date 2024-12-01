from collections import Counter
from heapq import heappush, heappop

heap_a, heap_b = [], []
freqs = Counter()
total_distance = similarity_score = 0

for line in open('input/day01', 'r').read().splitlines():
    a, b = line.split()
    heappush(heap_a, int(a))
    heappush(heap_b, int(b))
    freqs[int(b)] += 1

for _ in range(len(heap_a)):
    a = heappop(heap_a)
    total_distance += abs(a - heappop(heap_b))
    similarity_score += a * freqs[a]

print('Part 1:', total_distance)
print('Part 2:', similarity_score)
