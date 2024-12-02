def safe(report):
    increasing = report[0] < report[1]

    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]

        if increasing and diff <= 0 or not increasing and diff >= 0 or abs(diff) > 3:
            return False

    return True

def safe_with_tolerance(report):
    if safe(report):
        return True

    for i in range(len(report)):
        if safe(report[:i] + report[i + 1:]):
            return True

    return False

reports = [[int(x) for x in line.split()] for line in open('input/day02', 'r').read().splitlines()]
print('Part 1:', sum(map(safe, reports)))
print('Part 2:', sum(map(safe_with_tolerance, reports)))
