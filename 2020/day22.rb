require "set"

p1, p2 = File.read("input/day22").chomp.split("\n\n").map do |s|
  s.split("\n").drop(1).map(&:to_i)
end

def game(p1, p2)
  loop do
    x1 = p1.shift
    x2 = p2.shift

    if x1 > x2
      p1 += [x1, x2]
    else
      p2 += [x2, x1]
    end

    return p1 if p2.length == 0
    return p2 if p1.length == 0
  end
end

def rec_game(p1, p2)
  mem = Set.new

  loop do
    return [true, p1] if mem.include?([p1, p2])
    mem << [p1.dup, p2.dup]

    x1 = p1.shift
    x2 = p2.shift

    if p1.length >= x1 && p2.length >= x2
      p1_won, _ = rec_game(p1.take(x1), p2.take(x2))
    else
      p1_won = x1 > x2
    end

    if p1_won
      p1 += [x1, x2]
    else
      p2 += [x2, x1]
    end

    return [true, p1] if p2.length == 0
    return [false, p2] if p1.length == 0
  end
end

p = game(p1.dup, p2.dup)
puts "Part 1: #{p.map.with_index { |x, i| (p.length - i) * x }.reduce(:+)}"

_, y = rec_game(p1, p2)
puts "Part 2: #{y.map.with_index { |x, i| (y.length - i) * x }.reduce(:+)}"
