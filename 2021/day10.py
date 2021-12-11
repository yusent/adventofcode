def get_score(line):
    bracket_pairs = { '{': '}', '(': ')', '<': '>', '[': ']' }
    open_brackets = []
    syntax_error_points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
    autocomplete_points = { '(': 1, '[': 2, '{': 3, '<': 4 }

    for c in line:
        if c in bracket_pairs:
            open_brackets.append(c)
        elif any(open_brackets) and bracket_pairs[open_brackets[-1]] == c:
            open_brackets.pop()
        else:
            return -syntax_error_points[c]

    score = 0

    for bracket in open_brackets[::-1]:
        score = score * 5 + autocomplete_points[bracket]

    return score

if __name__ == "__main__":
    lines = open("input/day10", "r").read().strip().split('\n')
    syntax_error_total_score = 0
    autocomplete_scores = []

    for line in lines:
        x = get_score(line)

        if x < 0:
            syntax_error_total_score -= x
        else:
            autocomplete_scores.append(x)

    print("Part 1:", syntax_error_total_score)
    print("Part 2:", sorted(autocomplete_scores)[len(autocomplete_scores) // 2])
