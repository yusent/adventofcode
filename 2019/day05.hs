import Data.List.Split (splitOn)
import Data.Vector (fromList)
import IntCode (execUntilHalt)

main :: IO ()
main = do
  ops <- fromList . map read . splitOn "," <$> readFile "input/day05"
  putStrLn $ "Part 1: " ++ show (execUntilHalt ops [1])
  putStrLn $ "Part 2: " ++ show (execUntilHalt ops [5])
