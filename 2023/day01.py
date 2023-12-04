import re

def calibration_value(line):
    return int(line[0] + line[-1])

def words_to_digits(line):
    if line == '': return ''
    if line.startswith('one'): return '1' + words_to_digits(line[2:])
    if line.startswith('two'): return '2' + words_to_digits(line[2:])
    if line.startswith('three'): return '3' + words_to_digits(line[4:])
    if line.startswith('four'): return '4' + words_to_digits(line[4:])
    if line.startswith('five'): return '5' + words_to_digits(line[3:])
    if line.startswith('six'): return '6' + words_to_digits(line[3:])
    if line.startswith('seven'): return '7' + words_to_digits(line[4:])
    if line.startswith('eight'): return '8' + words_to_digits(line[4:])
    if line.startswith('nine'): return '9' + words_to_digits(line[3:])
    if line[0].isdigit(): return line[0] + words_to_digits(line[1:])
    return words_to_digits(line[1:])

calibration_data = open('input/day01', 'r').read().splitlines()
print('Part 1: ', sum(map(calibration_value, map(lambda x: re.sub(r'\D', '', x), calibration_data))))
print('Part 2: ', sum(map(calibration_value, map(words_to_digits, calibration_data))))
