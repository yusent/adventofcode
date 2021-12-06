import Data.List
import Data.List.Split

main = do
  (numsStr : boardsStrs) <- splitOn "\n\n" <$> readFile "input/day04"
  let nums = map read $ splitOn "," numsStr :: [Int]
      boards = parseBoard <$> boardsStrs
      (winner : scores) = play nums boards []
  putStrLn $ "Part 1: " ++ show winner
  putStrLn $ "Part 2: " ++ show (last scores)

parseBoard str = let rs = map read . words <$> lines str in (rs, transpose rs)

play _ [] scores = scores
play (num : nums) boards scores = play nums boards' scores'
  where
    (winnerBoards, boards') = partition won $ scratch num <$> boards
    scores' = scores ++ map (score num) winnerBoards

scratch n (rows, cols) = (filter (/= n) <$> rows, filter (/= n) <$> cols)

won (rows, cols) = any null rows || any null cols

score num = (* num) . sum . map sum . fst
