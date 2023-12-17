from functools import reduce

def hash(s):
    return reduce(lambda x, y: (x + ord(y)) * 17 % 256, s, 0)

def process_step(boxes, step):
    label, op, val = (step[:-2], step[-2], int(step[-1])) if step[-1].isdigit() else (step[:-1], step[-1], None)
    box_index = hash(label)

    if op == '-':
        boxes[box_index] = [lens for lens in boxes[box_index] if lens[0] != label]
    elif val is not None:
        for i, lens in enumerate(boxes[box_index]):
            if lens[0] == label:
                boxes[box_index][i] = (label, val)
                break
        else:
            boxes[box_index].append((label, val))

def process_and_get_focusing_power(steps):
    boxes = {i: [] for i in range(256)}
    for step in steps: process_step(boxes, step)
    return sum((i+1)*j*focal_len for i, lenses in boxes.items() for j, (label, focal_len) in enumerate(lenses, 1))

initialization_sequence = open('input/day15').read().strip().split(',')
print('Part 1:', sum(hash(s) for s in initialization_sequence))
print('Part 2:', process_and_get_focusing_power(initialization_sequence))
