def mcb(b):
    return '1' if sum(map(int, b)) >= len(b) / 2 else '0'

def power_consumption(bins):
    l = len(bins[0])
    gamma = ''.join(mcb(list(map(lambda b: b[i], bins))) for i in range(l))
    epsilon = ''.join('1' if b == '0' else '0' for b in gamma)
    return int(gamma, 2) * int(epsilon, 2)

def life_support_rating(bins, cmp):
    for i in range(len(bins[0])):
        if len(bins) == 1:
            return int(bins[0], 2)
        b = mcb(list(map(lambda b: b[i], bins)))
        bins = list(filter(lambda x: cmp(x[i], b), bins))

def oxygen_generator_rating(bins):
    return life_support_rating(bins, lambda a, b: a == b)

def co2_scrubber_rating(bins):
    return life_support_rating(bins, lambda a, b: a != b)

if __name__ == "__main__":
    bins = open("input/day03", "r").read().strip().split('\n')
    print("Part 1:", power_consumption(bins))
    print("Part 2:", oxygen_generator_rating(bins) * co2_scrubber_rating(bins))
