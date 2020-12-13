function move1 (pos, dir_idx, cmd, arg)
  local dirs = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}}
  local off_x = dirs[dir_idx + 1][1]
  local off_y = dirs[dir_idx + 1][2]

  if     cmd == "N" then return {pos[1], pos[2] + arg}, dir_idx
  elseif cmd == "S" then return {pos[1], pos[2] - arg}, dir_idx
  elseif cmd == "E" then return {pos[1] + arg, pos[2]}, dir_idx
  elseif cmd == "W" then return {pos[1] - arg, pos[2]}, dir_idx
  elseif cmd == "L" then return pos, (arg // 90 * 3 + dir_idx) % 4
  elseif cmd == "R" then return pos, (arg // 90 + dir_idx) % 4
  elseif cmd == "F" then return {pos[1] + off_x * arg, pos[2] + off_y * arg}, dir_idx
  end
end

function move2 (pos, waypoint, cmd, arg)
  if     cmd == "N" then return pos, {waypoint[1], waypoint[2] + arg}
  elseif cmd == "S" then return pos, {waypoint[1], waypoint[2] - arg}
  elseif cmd == "E" then return pos, {waypoint[1] + arg, waypoint[2]}
  elseif cmd == "W" then return pos, {waypoint[1] - arg, waypoint[2]}
  elseif cmd == "L" then return pos, rotate_left(waypoint, arg // 90)
  elseif cmd == "R" then return pos, rotate_right(waypoint, arg // 90)
  elseif cmd == "F" then return {pos[1] + waypoint[1] * arg, pos[2] + waypoint[2] * arg}, waypoint
  end
end

function rotate_left (waypoint, times)
  if times == 0 then return waypoint end

  return rotate_left({-waypoint[2], waypoint[1]}, times - 1)
end

function rotate_right (waypoint, times)
  if times == 0 then return waypoint end

  return rotate_right({waypoint[2], -waypoint[1]}, times - 1)
end

function main ()
  local pos1 = {0, 0}
  local pos2 = {0, 0}
  local dir_idx = 0
  local waypoint = {10, 1}

  for line in io.lines("input/day12") do
    local cmd = string.sub(line, 1, 1)
    local arg = tonumber(string.sub(line, 2))
    pos1, dir_idx = move1(pos1, dir_idx, cmd, arg)
    pos2, waypoint = move2(pos2, waypoint, cmd, arg)
  end

  print("Part 1:", math.abs(pos1[1]) + math.abs(pos1[2]))
  print("Part 2:", math.abs(pos2[1]) + math.abs(pos2[2]))
end

main()
