def generate_difference_pyramid(sequence):
    pyramid = [sequence]

    while any(x != 0 for x in pyramid[-1]):
        pyramid.append([pyramid[-1][i+1] - pyramid[-1][i] for i in range(len(pyramid[-1]) - 1)])

    return pyramid

def extrapolate_next_value(sequence):
    pyramid = generate_difference_pyramid(sequence)

    for i in range(len(pyramid) - 2, -1, -1):
        pyramid[i].append(pyramid[i][-1] + pyramid[i + 1][-1])

    return pyramid[0][-1]

def extrapolate_previous_value(sequence):
    pyramid = generate_difference_pyramid(sequence)
    pyramid[-1].insert(0, 0)

    for i in range(len(pyramid) - 2, -1, -1):
        new_first_value = pyramid[i][0] - pyramid[i + 1][0]
        pyramid[i].insert(0, new_first_value)

    return pyramid[0][0]

sequences = [[int(n) for n in line.split()] for line in open('input/day09').readlines()]

print('Part 1:', sum(map(extrapolate_next_value, sequences)))
print('Part 2:', sum(map(extrapolate_previous_value, sequences)))
