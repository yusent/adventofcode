main = do
  depths <- map read . lines <$> readFile "input/day01"
  putStrLn $ "Part 1: " ++ show (countIncrements 1 depths)
  putStrLn $ "Part 2: " ++ show (countIncrements 3 depths)

countIncrements :: Int -> [Int] -> Int
countIncrements size = length . filter (uncurry (<)) . (zip <*> drop size)
