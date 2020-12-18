def eval1(str)
  str.sub!(/\([^()]*\)/) { |m| eval1(m[1..-2]) } while str =~ /\(/
  str.sub!(/^\d+\s+.\s+\d+/) { |m| eval(m).to_s } while str =~ /^\d+\s+.\s+\d+/
  str
end

def eval2(str)
  str.sub!(/\([^()]*\)/) { |m| eval2(m[1..-2]) } while str =~ /\(/
  str.sub!(/\d+\s+\+\s+\d+/) { |m| eval(m).to_s } while str =~ /\d+\s+\+\s+\d+/
  str.sub!(/\d+\s+\*\s+\d+/) { |m| eval(m).to_s } while str =~ /\d+\s+\*\s+\d+/
  str
end

s, z = File.read("input/day18").chomp.split("\n").reduce([0, 0]) do |x, line|
  [x[0] + eval1(line.dup).to_i, x[1] + eval2(line).to_i]
end

puts "Part 1: #{s}"
puts "Part 2: #{z}"
