import Data.List (tails)

main = do
  depths <- map read . lines <$> readFile "input/day01"
  putStrLn $ "Part 1: " ++ show (countIncrements 1 depths)
  putStrLn $ "Part 2: " ++ show (countIncrements 3 depths)

countIncrements windowSize xs = fst $ foldl count (0, firstWindow) windows
  where
    (firstWindow : windows) = sum . take windowSize <$> tails xs
    count (acc, prev) x = (acc + fromEnum (x > prev), x)
