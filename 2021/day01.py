def count_increments(w, xs):
    return sum(1 if xs[i] > xs[i-w] else 0 for i in range(w, len(xs)))

if __name__ == "__main__":
    depths = list(map(int, open("input/day01", "r").read().split()))
    print("Part 1:", count_increments(1, depths))
    print("Part 2:", count_increments(3, depths))
