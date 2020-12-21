require "set"

allergens = {}
ingredients = {}

File.read("input/day21").chomp.split("\n").each do |line|
  ingredients_str, allergens_str = line[0..-2].split(" (contains ")

  ingredients_set = Set.new(ingredients_str.split.map do |ingredient|
    ingredients[ingredient] = ingredients[ingredient].to_i + 1
    ingredient
  end)

  allergens_str.split(", ").each do |allergen|
    allergens[allergen] = allergens.has_key?(allergen) \
      ? allergens[allergen] & ingredients_set \
      : ingredients_set
  end
end

loop do
  allergen_pair = allergens.find { |_, v| v.is_a?(Set) && v.size == 1 }

  break if allergen_pair.nil?

  allergen = allergen_pair[0]
  ingredient = allergen_pair[1].to_a[0]
  allergens[allergen] = ingredient
  ingredients.delete(ingredient)

  allergens.transform_values! { |s| s.is_a?(Set) ? s.delete(ingredient) : s }
end

puts "Part 1: #{ingredients.values.sum}"
puts "Part 2: #{allergens.sort.map { |_, v| v }.join(",")}"
