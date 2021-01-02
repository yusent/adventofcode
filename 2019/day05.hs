import IntCode (execUntilHalt, load)

main :: IO ()
main = do
  ops <- load <$> readFile "input/day05"
  putStrLn $ "Part 1: " ++ show (execUntilHalt ops [1])
  putStrLn $ "Part 2: " ++ show (execUntilHalt ops [5])
