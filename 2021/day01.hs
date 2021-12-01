import Data.List (tails)

main = do
  depths <- map read . lines <$> readFile "input/day01"
  putStrLn $ "Part 1: " ++ show (countIncrements depths)
  putStrLn $ "Part 2: " ++ show (countWindowIncrements depths)

countWindowIncrements =
  countIncrements . map sum . filter ((>2) . length) . map (take 3) . tails

countIncrements :: [Int] -> Int
countIncrements (x : xs) = countIncrements' 0 x xs

countIncrements' count _ [] = count
countIncrements' count prev (x : xs) =
  countIncrements' (count + fromEnum (x > prev)) x xs
