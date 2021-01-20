import Data.List.Split (splitOn)
import qualified Data.Map as M (Map, (!?), empty, insert)
import Data.Set (delete, empty, insert, size)
import IntCode (State(..), addInput, changeInstructionAt, getOutput, load, run)

type Screen = M.Map (Int, Int) Int

main :: IO ()
main = do
  ops <- load <$> readFile "input/day13"
  -- Use an empty file to play interactively
  part2Moves <- map read . splitOn "," <$> readFile "input/day13-part2-moves"
  let Halted outputs = run $ Initial ops []
      part1 = countBlockTiles outputs
  putStrLn $ "Part 1: " ++ show part1
  playGame part2Moves 0 M.empty . run $ Initial (changeInstructionAt 0 2 ops) []

countBlockTiles :: [Int] -> Int
countBlockTiles = count empty
  where
    count blocksSet (2 : y : x : rest) = count (insert (x, y) blocksSet) rest
    count blocksSet (_ : y : x : rest) = count (delete (x, y) blocksSet) rest
    count blocksSet _ = size blocksSet

playGame :: [Int] -> Int -> Screen -> State -> IO ()
playGame inputs score screen state = do
  let (newScore, newScreen) = move score screen $ getOutput state
  case (inputs, state) of
    (input : inputs', WaitingForInput {}) -> do
      playGame inputs' newScore newScreen . run $ addInput state input

    ([], WaitingForInput {}) -> do
      putStrLn $ "SCORE: " ++ show newScore
      putStrLn $ screenToString newScreen
      putStrLn "Insert Input:"
      putStrLn "(h) move left, (l) move right, (anything else) don't move"
      cmd <- getLine
      let input
            | cmd == "h" = -1
            | cmd == "l" = 1
            | otherwise = 0
      playGame [] newScore newScreen . run $ addInput state input

    _ -> putStrLn $ "Part 2: " ++ show newScore

move :: Int -> Screen -> [Int] -> (Int, Screen)
move _ acc (newScore : 0 : -1 : rest) = move newScore acc rest
move score acc (t : y : x : rest) = move score (M.insert (x, y) t acc) rest
move score acc [] = (score, acc)

screenToString :: Screen -> String
screenToString screen = unlines $ do
  y <- [0..20]
  return $ do
    x <- [0..34]
    let char = case screen M.!? (x, y) of
                 Just 1 -> '|'
                 Just 2 -> '#'
                 Just 3 -> '='
                 Just 4 -> 'O'
                 _ -> ' '
    return char
