mem1 = {}
mem2 = {}
mask = nil

File.read("input/day14").chomp.split("\n").each do |line|
  match_mask = line.match(/^mask = (.*)$/)

  if match_mask
    mask = match_mask[1]
    next
  end

  match = line.match(/^mem\[(\d+)\] = (\d+)$/)
  part1_value = ""
  part2_addresses = [""]
  binary_address = "%036b" % match[1]
  binary_value = "%036b" % match[2]

  36.times do |i|
    if mask[i] == "X"
      part1_value << binary_value[i]
      part2_addresses = part2_addresses.map { |a| %W(#{a}0 #{a}1) }.flatten
    else
      part1_value << mask[i]
      address_bit = mask[i] == "0" ? binary_address[i] : "1"
      part2_addresses.each { |a| a << address_bit }
    end
  end

  mem1[match[1]] = part1_value.to_i(2)
  part2_addresses.each { |address| mem2[address] = match[2].to_i }
end

puts "Part 1: #{mem1.values.reduce(:+)}"
puts "Part 2: #{mem2.values.reduce(:+)}"
