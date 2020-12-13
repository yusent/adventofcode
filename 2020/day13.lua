function mult_inv(a, b)
  if b == 1 then return 1 end

  local b0 = b
  local x0 = 0
  local x1 = 1

  while a > 1 do
    x0, x1 = x1 - math.floor(a / b) * x0, x0
    a, b = b, math.fmod(a, b)
  end

  return x1 % b0
end

function product (x, ...) return x and x * product(...) or 1 end

function chinese_remainder (n, a)
  local prod = product(table.unpack(n))
  local sum = 0

  for i = 1, #n do
    local p = prod / n[i]
    sum = sum + a[i] * mult_inv(p, n[i]) * p
  end

  return math.fmod(sum, prod)
end

function main ()
  local input_file = io.open("input/day13")
  local timestamp = input_file:read("*n")
  local min_wait
  local bus_id
  local buses = {}
  local mods = {}
  local t = 0

  for bus_id_str in string.gmatch(input_file:read("*a"), "%w+") do
    local bus_id_num = tonumber(bus_id_str)

    if bus_id_num then
      local wait_time = (bus_id_num - timestamp) % bus_id_num

      if not bus_id or wait_time < min_wait then
        bus_id = bus_id_num
        min_wait = wait_time
      end

      table.insert(buses, bus_id_num)
      table.insert(mods, (bus_id_num - t) % bus_id_num)
    end

    t = t + 1
  end

  input_file:close()

  print("Part 1:", min_wait * bus_id)
  print("Part 2:", string.format("%.0f", chinese_remainder(buses, mods)))
end

main()
