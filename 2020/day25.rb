pkey1, pkey2 = 6270530, 14540258
value, loop_size = 1, 0
value, loop_size = (value * 7) % 20201227, loop_size + 1 while value != pkey1
puts loop_size.times.reduce(1) { |v, _| (v * pkey2) % 20201227 }
