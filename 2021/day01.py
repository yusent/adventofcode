def count_increments(window_size, xs):
    increments = 0
    prev = sum(xs[:window_size])

    for i in range(1, len(xs) - window_size + 1):
        s = sum(xs[i:i+window_size])

        if s > prev:
            increments += 1

        prev = s

    return increments

if __name__ == "__main__":
    depths = list(map(int, open("input/day01", "r").read().split()))
    print("Part 1:", count_increments(1, depths))
    print("Part 2:", count_increments(3, depths))
