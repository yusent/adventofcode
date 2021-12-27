from itertools import product

def find_valid_model_number(digits, increments, mods):
    z = 0
    res = [0] * 14
    digits_idx = 0

    for i in range(14):
        if increments[i] is None:
            res[i] = z % 26 - mods[i]
            z //= 26

            if not 1 <= res[i] <= 9:
                return False
        else:
            z = z * 26 + digits[digits_idx] + increments[i]
            res[i] = digits[digits_idx]
            digits_idx += 1

    return res

def solve(range_, increments, mods):
    for digits in product(range_, repeat=7):
        res = find_valid_model_number(digits, increments, mods)

        if res:
            return "".join(map(str, res))

def parse(input_file):
    lines, increments, mods = input_file.split("\n"), [None] * 14, [None] * 14

    for i in range(14):
        r = int(lines[i*18+5].split()[2])

        if r > 9:
            increments[i] = int(lines[i*18+15].split()[2])
        else:
            mods[i] = -r

    return increments, mods

if __name__ == "__main__":
    increments, mods = parse(open("input/day24").read().strip())
    print("Part 1:", solve(range(9, 0, -1), increments, mods))
    print("Part 2:", solve(range(1, 10), increments, mods))
