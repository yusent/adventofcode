main = do
  positions <- map read . splitByCommas <$> readFile "input/day07"
  putStrLn $ "Part 1: " ++ show (bestPosition (\s d -> abs $ s - d) positions)
  putStrLn $ "Part 2: " ++ show (bestPosition fuelExpense positions)
  where splitByCommas = words . map (\c -> if c == ',' then ' ' else c)

bestPosition expenseFunc positions =
  minimum [sum (expenseFunc p <$> positions) | p <- [0..maximum positions]]

fuelExpense src dst = let n = abs (src - dst) in n * (n + 1) `div` 2
