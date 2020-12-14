main :: IO ()
main = do
  modules <- map read . lines <$> readFile "input/day01"
  putStrLn . ("Part 1: " ++) . show . sum $ requiredFuel <$> modules
  putStrLn . ("Part 2: " ++) . show . sum $ totalRequiredFuel <$> modules

requiredFuel :: Int -> Int
requiredFuel = subtract 2 . flip div 3

totalRequiredFuel :: Int -> Int
totalRequiredFuel module'
  | module' < 9 = 0
  | otherwise = let f = requiredFuel module' in f + totalRequiredFuel f
