depths = list(map(int, open("input/day01", "r").read().split()))
prev = depths[0]
prev_window = sum(depths[:3])
increments = 0
window_increments = 0

for i in range(1, len(depths)):
    if depths[i] > prev:
        increments += 1

    prev = depths[i]

    if i + 2 < len(depths):
        window = sum(depths[i:i+3])

        if window > prev_window:
            window_increments += 1

        prev_window = window

print("Part 1:", increments)
print("Part 2:", window_increments)
