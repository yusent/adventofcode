main = do
  commands <- map words . lines <$> readFile "input/day02"
  let (x1, depth1) = foldl exec1 (0, 0) commands
      (x2, depth2, _) = foldl exec2 (0, 0, 0) commands
  putStrLn $ "Part 1: " ++ show (x1 * depth1)
  putStrLn $ "Part 2: " ++ show (x2 * depth2)

exec1 (x, depth) ["forward", steps] = (x + read steps, depth)
exec1 (x, depth) ["down", steps] = (x, depth + read steps)
exec1 (x, depth) ["up", steps] = (x, depth - read steps)

exec2 (x, depth, aim) ["forward", steps] = let s = read steps in (x + s, depth + aim * s, aim)
exec2 (x, depth, aim) ["down", steps] = (x, depth, aim + read steps)
exec2 (x, depth, aim) ["up", steps] = (x, depth, aim - read steps)
