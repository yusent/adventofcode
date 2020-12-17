require "set"

input = File.read("input/day16").chomp
constraints_str, my_ticket_str, tickets_str = input.split("\n\n")
my_ticket = my_ticket_str.split("\n")[1].split(",").map(&:to_i)
tickets = tickets_str.split("\n").drop(1).map { |t| t.split(",").map(&:to_i) }

constraints, h = constraints_str.split("\n").reduce([{}, {}]) do |acc, c|
  constraints, h = acc
  m = c.match(/^(.+): (\d+)-(\d+) or (\d+)-(\d+)$/)
  ranges = m.to_a.drop(2).map(&:to_i)
  [
    constraints.merge({ m[1] => ranges }),
    h.merge({ m[1] => Set.new((0..tickets[0].length - 1).to_a) }),
  ]
end

scanning_err_rate = tickets.reduce(0) do |acc, ticket|
  valid, scanning_err_rate = ticket.reduce([true, 0]) do |(valid, err_rate), v|
    constraints.values.any? do |c|
      (v >= c[0] && v <= c[1]) || (v >= c[2] && v <= c[3])
    end ? [valid, err_rate] : [false, err_rate + v]
  end

  if valid
    h_ = constraints.map { |name, _| [name, Set[]] }.to_h

    ticket.each_with_index do |v, i|
      constraints.each do |name, c|
        if (v >= c[0] && v <= c[1]) || (v >= c[2] && v <= c[3])
          h_[name] << i
        end
      end
    end

    h_.each do |name, s|
      h[name] = h[name] & s
    end

    acc
  else
    acc + scanning_err_rate
  end
end

indexes = (0..my_ticket.length - 1).to_a

while h.values.any? { |v| v.is_a? Set } do
  h.each do |name, values|
    if values.is_a?(Set) && values.size == 1
      value = values.to_a[0]
      h[name] = value

      h.each do |name, values|
        if values.is_a?(Set)
          h[name] = values.delete(value)
        end
      end

      break
    end
  end

  indexes.each do |index|
    h_ = h.select { |k, v| v.is_a?(Set) && v.include?(index) }

    if h_.size == 1
      h_.each { |k, v| h[k] = index }
      indexes.delete(index)
      break
    end
  end
end

departure_prod = h
  .select { |k, s| k =~ /^departure/ }
  .values
  .reduce(1) { |acc, i| acc * my_ticket[i] }

puts "Part 1: #{scanning_err_rate}"
puts "Part 2: #{departure_prod}"
