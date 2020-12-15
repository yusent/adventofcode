import Data.Map.Strict (Map, (!?), fromList, insert)

main :: IO ()
main = do
  let input = fromList [(2, 1), (1, 2), (10, 3), (11, 4), (0, 5)]
  putStrLn . ("Part 1: " ++) . show $ entries input 6 2020 6
  putStrLn . ("Part 2: " ++) . show $ entries input 6 30000000 6

entries :: Map Int Int -> Int -> Int -> Int -> Int
entries m i u n
  | i == u = n
  | otherwise = seq n . entries (insert n i m) (i + 1) u . maybe 0 (i -) $ m !? n
