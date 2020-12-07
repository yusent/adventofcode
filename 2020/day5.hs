import Data.List (sort)

main :: IO ()
main = do
  let seatID str = row str * 8 + col str
      row = binarySpacePos 'B' 7 . take 7
      col = binarySpacePos 'R' 3 . drop 7
      findMissing (a : b : rest)
        | a + 1 == b = findMissing (b : rest)
        | otherwise = a + 1

  seats <- sort . map seatID . lines <$> readFile "input/day5"

  putStrLn $ "Part 1: " ++ show (last seats)
  putStrLn $ "Part 2: " ++ show (findMissing seats)

binarySpacePos :: Char -> Int -> String -> Int
binarySpacePos upperChar len = fst . foldl folder (0, 0)
  where
    folder (pos, index) char
      | char == upperChar = (pos + 2 ^ (len - index - 1), index + 1)
      | otherwise = (pos, index + 1)
