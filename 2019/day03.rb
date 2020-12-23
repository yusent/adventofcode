p1, p2 = File.read("input/day03").chomp.split("\n").map do |line|
  x, y = 0, 0

  line.split(",").map do |s|
    steps = s[1..-1].to_i

    case s[0]
    when "U"
      y += steps
    when "D"
      y -= steps
    when "R"
      x += steps
    when "L"
      x -= steps
    end

    [x, y]
  end
end

intersections = []
prev_x1, prev_y1, steps1 = 0, 0, 0

p1.each do |x1, y1|
  min_x1 = [prev_x1, x1].min
  max_x1 = [prev_x1, x1].max
  min_y1 = [prev_y1, y1].min
  max_y1 = [prev_y1, y1].max
  prev_x2, prev_y2, steps2 = 0, 0, 0

  p2.each do |x2, y2|
    min_x2 = [prev_x2, x2].min
    max_x2 = [prev_x2, x2].max
    min_y2 = [prev_y2, y2].min
    max_y2 = [prev_y2, y2].max

    if min_x1 <= max_x2 && min_x2 <= max_x1 && min_y1 <= max_y2 && min_y2 <= max_y1
      if prev_x1 == x1
        ix = x1
        iy = y2
        steps_to_i2 = (ix - prev_x2).abs
        steps_to_i1 = (iy - prev_y1).abs
      else
        ix = x2
        iy = y1
        steps_to_i1 = (ix - prev_x1).abs
        steps_to_i2 = (iy - prev_y2).abs
      end

      intersections.push({
        distance: ix.abs + iy.abs,
        steps_sum: steps1 + steps_to_i1 + steps2 + steps_to_i2,
      })
    end

    steps2 += (x2 - prev_x2).abs + (y2 - prev_y2).abs
    prev_x2, prev_y2 = x2, y2
  end

  steps1 += (x1 - prev_x1).abs + (y1 - prev_y1).abs
  prev_x1, prev_y1 = x1, y1
end

intersections.shift
puts "Part 1: #{intersections.map { |i| i[:distance] }.min}"
puts "Part 2: #{intersections.map { |i| i[:steps_sum] }.min}"
