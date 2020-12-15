input = {[2] = 1, [1] = 2, [10] = 3, [11] = 4, [0] = 5}
orig_len = 6
current_num = 6

for i = 1, 30000000 - orig_len do
  prev_index = input[current_num]
  input[current_num] = orig_len + i - 1
  current_num = prev_index and (orig_len + i - 1 - prev_index) or 0
  if i == 2020 - orig_len then print("Part 1:", current_num) end
end

print("Part 2:", current_num)
