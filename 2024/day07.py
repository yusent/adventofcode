def parse_calibration(line):
    first, *rest = line.split()
    return int(first[:-1]), list(map(int, rest))

def possible_equations(operands, operators='+*'):
    match operands:
        case [operand]:
            yield [operand]

        case [operand, *rest]:
            for operator in operators:
                for equation in possible_equations(rest, operators):
                    yield [operand, operator, *equation]

def eval_equation(equation):
    match equation:
        case [operand]:
            return operand

        case [op0, '||', op1, *rest]:
            return eval_equation([int(f'{op0}{op1}'), *rest])

        case [op0, operator, op1, *rest]:
            return eval_equation([eval(f'{op0}{operator}{op1}'), *rest])

def calc_total_calibration(calibrations, operators='+*'):
    total_calibration = 0

    for test_value, operands in calibrations:
        for equation in possible_equations(operands, operators):
            if eval_equation(equation) == test_value:
                total_calibration += test_value
                break

    return total_calibration

calibrations = list(map(parse_calibration, open('input/day07', 'r').read().splitlines()))

print('Part 1:', calc_total_calibration(calibrations))
print('Part 2:', calc_total_calibration(calibrations, ['*', '+', '||']))
