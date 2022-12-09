from collections import Counter
from pathlib import Path

curr_path = Path('/')
fs = Counter()

for line in open('input/day07', 'r').read().split('\n'):
    match line.split():
        case ['$', 'cd', newdir]:
            curr_path = (curr_path / newdir).resolve()
        case [size, _] if size.isdigit():
            for path in [*curr_path.parents, curr_path]: fs[path] += int(size)

to_remove = 30_000_000 + fs[Path('/')] - 70_000_000

print('Part 1:', sum(size for size in fs.values() if size <= 100_000))
print('Part 2:', min(size for size in fs.values() if size >= to_remove))
