def defrag(expansion):
    left, right = 0, len(expansion) - 1

    while left < right:
        if expansion[left] != '.':
            left += 1
            continue

        if expansion[right] == '.':
            right -= 1
            continue

        expansion[left], expansion[right] = expansion[right], expansion[left]

def move_file(expansion, start, end, free_spaces):
    file_size = end - start + 1

    for space_start, space_size in free_spaces:
        if space_size >= file_size and space_start < start:
            for i in range(file_size):
                expansion[space_start + i] = expansion[start + i]
                expansion[start + i] = '.'

            new_space_start = space_start + file_size
            new_space_size = space_size - file_size
            free_spaces.remove((space_start, space_size))

            if new_space_size > 0:
                free_spaces.append((new_space_start, new_space_size))

            free_spaces.append((start, file_size))
            free_spaces.sort()
            return

def defrag_v2(expansion):
    free_spaces = []
    end = 0

    while end < len(expansion):
        if expansion[end] == '.':
            start = end
            while end < len(expansion) and expansion[end] == '.':
                end += 1
            free_spaces.append((start, end - start))
        else:
            end += 1

    end = len(expansion) - 1

    while end >= 0:
        if expansion[end] == '.':
            end -= 1
            continue

        start = end

        while start > 0 and expansion[start - 1] == expansion[end]:
            start -= 1

        move_file(expansion, start, end, free_spaces)
        end = start - 1

def checksum(expansion):
    return sum(i * x for i, x in enumerate(expansion) if x != '.')

disk_map = open('input/day09').read().strip()
disk_expansion = []

for i, block_size in enumerate(disk_map):
    expansion = [i // 2 if i % 2 == 0 else '.'] * int(block_size)
    disk_expansion.extend(expansion)

v2_disk_expansion = disk_expansion.copy()
defrag(disk_expansion)
print('Part 1:', checksum(disk_expansion))
defrag_v2(v2_disk_expansion)
print('Part 2:', checksum(v2_disk_expansion))
