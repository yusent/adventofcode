main = do
  commands <- map (parse . words) . lines <$> readFile "input/day02"
  putStrLn $ "Part 1: " ++ show (run exec1 commands)
  putStrLn $ "Part 2: " ++ show (run exec2 commands)

parse [direction, steps] = (direction, read steps)

run execFunc = mult . foldl execFunc (0, 0, 0)

mult (a, b, _) = a * b

exec1 (x, depth, _) ("forward", steps) = (x + steps, depth, 0)
exec1 (x, depth, _) ("down", steps) = (x, depth + steps, 0)
exec1 (x, depth, _) ("up", steps) = (x, depth - steps, 0)

exec2 (x, depth, aim) ("forward", steps) = (x + steps, depth + aim * steps, aim)
exec2 (x, depth, aim) ("down", steps) = (x, depth, aim + steps)
exec2 (x, depth, aim) ("up", steps) = (x, depth, aim - steps)
