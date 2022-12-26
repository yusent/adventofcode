mem = {}

for line in open('input/day21').read().splitlines():
    name, op = line.split(': ')
    if op.isnumeric():
        mem[name] = int(op)
        continue
    op0, op, op1 = op.split(' ')
    mem[name] = eval(f'lambda: solve("{op0}") {op} solve("{op1}")')
    if name == 'root': root_ops = [op0, op1]

solve = lambda name: mem[name] if isinstance(mem[name], int) else mem[name]()

print('Part 1:', int(solve('root')))

before_humn_modif = solve(root_ops[0])
mem['humn'] = 0
op, target_op = root_ops if before_humn_modif != solve(root_ops[0]) else reversed(root_ops)
lo, hi, target = 0, int(1e24), solve(target_op)

while True:
    mem['humn'] = (lo + hi) // 2
    diff = target - solve(op)
    if diff < 0: lo = mem['humn']
    elif diff > 0: hi = mem['humn']
    else: break

print('Part 2:', mem['humn'])
