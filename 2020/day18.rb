def eval_(s, p2 = false)
  s.sub!(/\([^()]*\)/) { |m| eval_(m[1..-2], p2) } while s =~ /\(/
  s.sub!(/\d+\s+.\s+\d+/) { |m| eval(m).to_s } while !p2 && s =~ /\d+\s+./
  s.sub!(/\d+\s+\+\s+\d+/) { |m| eval(m).to_s } while p2 && s =~ /\d+\s+\+/
  s.sub!(/\d+\s+\*\s+\d+/) { |m| eval(m).to_s } while p2 && s =~ /\d+\s+\*/
  s
end

c1, c2 = File.read("input/day18").chomp.split("\n").reduce([0, 0]) do |x, line|
  [x[0] + eval_(line.dup).to_i, x[1] + eval_(line, true).to_i]
end

puts "Part 1: #{c1}"
puts "Part 2: #{c2}"
