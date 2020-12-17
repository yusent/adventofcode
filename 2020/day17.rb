def build(coords, dimensions)
  coords.map do |x, y|
    [[x, y, *Array.new(dimensions - 2).fill(0)], 0]
  end.to_h
end

def neighbours_step(acc, coords)
  return acc if coords.empty?

  new_acc = [-1, 0, 1].map do |offset|
    acc.map { |prev| [*prev, coords[0] + offset] }
  end.flatten(1)

  neighbours_step(new_acc, coords.drop(1))
end

def neighbours(coords)
  neighbours_step([[]], coords).reject { |c| c == coords }
end

def evolve(gens, grid)
  return grid if gens == 0

  new = {}

  grid.each_key do |coords|
    neighbours(coords).each do |neighbour|
      if grid.has_key?(neighbour)
        grid[neighbour] += 1
      else
        new[neighbour] = new[neighbour].to_i + 1
      end
    end
  end

  grid.each do |coords, nbrs_count|
    if nbrs_count >= 2 && nbrs_count <= 3
      grid[coords] = 0
    else
      grid.delete(coords)
    end
  end

  new.each { |coords, nbrs_count| grid[coords] = 0 if nbrs_count == 3 }

  evolve(gens - 1, grid)
end

coords = []

File.read("input/day17").chomp.split("\n").each_with_index do |line, y|
  line.chars.each_with_index { |c, x| coords.push([x, y]) if c == "#" }
end

puts "Part 1: #{evolve(6, build(coords, 3)).size}"
puts "Part 2: #{evolve(6, build(coords, 4)).size}"
