main :: IO ()
main = do
  rows <- lines <$> readFile "input/day3"
  let width = length $ head rows
      count = countTrees width rows 0 0
      part1 = count 3 1
      part2 = part1 * count 1 1 * count 5 1 * count 7 1 * count 1 2
  putStrLn $ "Part 1: " ++ show part1
  putStrLn $ "Part 2: " ++ show part2

countTrees :: Int -> [String] -> Int -> Int -> Int -> Int -> Int
countTrees width rows col count right down
  | null remainingRows = count
  | otherwise = countTrees width remainingRows newCol newCount right down
  where
    remainingRows = drop down rows
    newCount = if char == '#' then count + 1 else count
    char = head remainingRows !! newCol
    newCol = (col + right) `mod` width
