def simulate(seed, days):
    count = len(seed)
    prods = [0] * days

    for age in seed:
        prods[age] += 1

    for day, prod in enumerate(prods):
        if prod > 0:
            if day + 7 < days:
                prods[day + 7] += prod

            if day + 9 < days:
                prods[day + 9] += prod

            count += prod

    return count

if __name__ == "__main__":
    seed = list(map(int, open("input/day06", "r").read().strip().split(',')))
    print("Part 1:", simulate(seed, 80))
    print("Part 2:", simulate(seed, 256))
