import Data.Set (delete, empty, insert, size)
import IntCode (State(..), load, run)

main :: IO ()
main = do
  ops <- load <$> readFile "input/day13"
  let Halted outputs = run $ Initial ops []
      part1 = countBlockTiles outputs
  putStrLn $ "Part 1: " ++ show part1

countBlockTiles :: [Int] -> Int
countBlockTiles = count empty
  where
    count blocksSet (2 : y : x : rest) = count (insert (x, y) blocksSet) rest
    count blocksSet (_ : y : x : rest) = count (delete (x, y) blocksSet) rest
    count blocksSet _ = size blocksSet
