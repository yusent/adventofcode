function mult_inv(a, b)
  local b0 = b
  local x0 = 0
  local x1 = 1

  if b == 1 then return 1 end

  while a > 1 do
    local q = math.floor(a / b)
    local amb = math.fmod(a, b)
    a = b
    b = amb
    local xqx = x1 - q * x0
    x1 = x0
    x0 = xqx
  end

  if x1 < 0 then x1 = x1 + b0 end

  return x1
end

function chinese_remainder (n, a)
  local prod = 1

  for _, x in ipairs(n) do
    prod = prod * x
  end

  local p
  local sm = 0

  for i = 1, #n do
    p = prod / n[i]
    sm = sm + a[i] * mult_inv(p, n[i]) * p
  end

  return math.fmod(sm, prod)
end

function main ()
  local timestamp
  local min_wait
  local bus_id
  local buses = {}
  local mods = {}

  for line in io.lines("input/day13") do
    if not timestamp then
      timestamp = tonumber(line)
    else
      local t = 0

      for bus_id_str in string.gmatch(line, "[^,]+") do
        local bus_id_num = tonumber(bus_id_str)

        if bus_id_num then
          local rem = timestamp % bus_id_num
          local wait_time = rem == 0 and 0 or (bus_id_num - rem)

          if not bus_id or wait_time < min_wait then
            bus_id = bus_id_num
            min_wait = wait_time
          end

          table.insert(buses, bus_id_num)
          table.insert(mods, (bus_id_num - t) % bus_id_num)
        end

        t = t + 1
      end
    end
  end

  print("Part 1:", min_wait * bus_id)
  print("Part 2:", string.format("%16.0f", chinese_remainder(buses, mods)))
end

main()
