function main ()
  local adapters = {0}
  local one_diffs = 0
  local three_diffs = 0
  local possible_arrangements = {}

  for line in io.lines("input/day10") do
    table.insert(adapters, tonumber(line))
  end

  table.sort(adapters)
  table.insert(adapters, adapters[#adapters] + 3)

  for i, adapter in ipairs(adapters) do
    if adapter - 1 == adapters[i - 1] then one_diffs = one_diffs + 1 end
    if adapter - 3 == adapters[i - 1] then three_diffs = three_diffs + 1 end
  end

  print("Part 1:", one_diffs * three_diffs)
  print('Part 2:', count_arrangements_from(1, adapters, possible_arrangements))
end

function count_arrangements_from (i, adapters, possible_arrangements)
  if i == #adapters then return 1 end
  if possible_arrangements[i] then return possible_arrangements[i] end

  local ans = 0

  for j = i + 1, #adapters, 1 do
    if adapters[j] - adapters[i] <= 3 then
      ans = ans + count_arrangements_from(j, adapters, possible_arrangements)
    end
  end

  possible_arrangements[i] = ans
  return ans
end

main()
