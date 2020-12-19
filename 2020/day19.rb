def gen_regex_step(rules, id, p2)
  rule = rules[id]

  return rule if rule.is_a?(String)

  if rule[0].is_a?(String)
    if p2 && id == "11"
      x, y = rule.map { |id_| gen_regex_step(rules, id_, p2) }
      "#{x}(#{x}(#{x}(#{x}#{y})?#{y})?#{y})?#{y}"
    else
      res = rule.map { |id_| gen_regex_step(rules, id_, p2) }.join
      p2 && id == "8" ? res + "+" : res
    end
  else
    "(#{rule.map do |ids|
      ids.map { |id_| gen_regex_step(rules, id_, p2) }.join
    end.join('|')})"
  end
end

def gen_regex(rules, p2 = false)
  Regexp.new("^#{gen_regex_step(rules, '0', p2)}$")
end

rules_str, strings = File.read("input/day19").chomp.split("\n\n")

rules = rules_str.split("\n").reduce({}) do |acc, string|
  if m = string.match(/^(\d+):((?: \d+)+)$/)
    value = m[2].strip.split
  elsif m = string.match(/^(\d+):((?: \d+)+) \|((?: \d+)+)$/)
    value = [m[2].strip.split, m[3].strip.split]
  elsif m = string.match(/^(\d+): "([ab])"$/)
    value = m[2]
  end
  acc.merge({ m[1] => value })
end

regex1 = gen_regex(rules)
regex2 = gen_regex(rules, true)

c1, c2 = strings.split("\n").reduce([0, 0]) do |(c1, c2), string|
  [c1 + (string =~ regex1 ? 1 : 0), c2 + (string =~ regex2 ? 1 : 0)]
end

puts "Part 1: #{c1}"
puts "Part 2: #{c2}"
