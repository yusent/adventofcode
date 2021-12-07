def fuel_expense(src, dest):
    n = abs(src - dest)
    return n * (n + 1) // 2

def best_pos_to_align(positions):
    min_fuel = None
    for position in range(positions[-1] + 1):
        fuel = sum(fuel_expense(p, position) for p in positions)
        if min_fuel is None or fuel < min_fuel:
            min_fuel = fuel
    return min_fuel

if __name__ == "__main__":
    poss = list(map(int, open("input/day07", "r").read().split(',')))
    poss.sort()
    mid = poss[len(poss) // 2]

    print("Part 1:", sum(abs(pos - mid) for pos in poss))
    print("Part 2:", best_pos_to_align(poss))
