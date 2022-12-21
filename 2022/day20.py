from collections import deque

p1_nums = list(map(int, open('input/day20').read().splitlines()))
p2_nums = list(map(lambda n: n * 811_589_153, p1_nums))
size = len(list(p1_nums))

def mix(nums, times):
    for _ in range(times):
        for i in range(size):
            while nums[0][0] != i: nums.append(nums.popleft())
            num = nums.popleft()
            for _ in range(num[1] % (size - 1)): nums.append(nums.popleft())
            nums.append(num)
    return nums

def sum_grove_coords(nums):
    i = [n for _, n in nums].index(0)
    at = lambda j: nums[j % size][1]
    return at(i + 1000) + at(i + 2000) + at(i + 3000)

print('Part 1:', sum_grove_coords(mix(deque(list(enumerate(p1_nums))), 1)))
print('Part 2:', sum_grove_coords(mix(deque(list(enumerate(p2_nums))), 10)))
