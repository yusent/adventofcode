import Data.Char (isDigit)

main :: IO ()
main = do
  (c1, c2) <- foldl count (0, 0) . lines <$> readFile "input/day2"
  putStrLn $ "Part 1: " ++ show c1 ++ "\nPart 2: " ++ show c2

count :: (Int, Int) -> String -> (Int, Int)
count (c1, c2) line =
  let p = parseLine line
  in (c1 + if check1 p then 1 else 0, c2 + if check2 p then 1 else 0)

parseLine :: String -> (Int, Int, Char, String)
parseLine line = (read l, read r, char, password)
  where
    (l, '-' : line') = span isDigit line
    (r, ' ' : char : ':' : ' ' : password) = span isDigit line'

check1 :: (Int, Int, Char, String) -> Bool
check1 (l, r, char, pwd) = occurrences >= l && occurrences <= r
  where
    occurrences = length $ filter (== char) pwd

check2 :: (Int, Int, Char, String) -> Bool
check2 (l, r, char, pwd) = (pwd !! (l - 1) == char) /= (pwd !! (r - 1) == char)
