from collections import Counter

def solve_for(number_of_steps, s, subs):
    pair_freqs = Counter()
    result_freqs = Counter()

    for i in range(len(s) - 1):
        pair_freqs[s[i:i+2]] += 1

    for _ in range(number_of_steps):
        freqs = Counter()

        for pair in pair_freqs:
            freqs[pair[0] + subs[pair]] += pair_freqs[pair]
            freqs[subs[pair] + pair[1]] += pair_freqs[pair]

        pair_freqs = freqs

    for pair in pair_freqs:
        result_freqs[pair[0]] += pair_freqs[pair]

    result_freqs[s[-1]] += 1

    return max(result_freqs.values()) - min(result_freqs.values())

if __name__ == "__main__":
    lines = open("input/day14", "r").read().strip().split("\n")
    s = lines[0]
    subs = {}

    for line in lines[2:]:
        pair, char = line.split(" -> ")
        subs[pair] = char

    print("Part 1:", solve_for(10, s, subs))
    print("Part 2:", solve_for(40, s, subs))
