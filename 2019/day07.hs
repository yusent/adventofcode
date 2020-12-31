import Control.Monad (guard)
import Data.List (nub)
import Data.List.Split (splitOn)
import Data.Maybe (fromJust)
import Data.Vector (Vector, fromList)
import IntCode (State(..), addInput, execUntilHalt, getOutput, run)

main :: IO ()
main = do
  ops <- fromList . map read . splitOn "," <$> readFile "input/day07"
  putStrLn $ "Part 1: " ++ show (findLargestOutput ops)
  putStrLn $ "Part 2: " ++ show (findLargestOutput' ops)

findLargestOutput :: Vector Int -> Int
findLargestOutput ops = maximum $ do
  a <- [0..4]
  b <- [0..4]
  c <- [0..4]
  d <- [0..4]
  e <- [0..4]
  let amps = [a, b, c, d, e]
      outputA = execUntilHalt ops [a, 0]
      outputB = execUntilHalt ops [b, outputA]
      outputC = execUntilHalt ops [c, outputB]
      outputD = execUntilHalt ops [d, outputC]
      outputE = execUntilHalt ops [e, outputD]
  guard $ nub amps == amps
  return outputE

findLargestOutput' :: Vector Int -> Int
findLargestOutput' ops = maximum $ do
  a <- [5..9]
  b <- [5..9]
  c <- [5..9]
  d <- [5..9]
  e <- [5..9]
  let amps = [a, b, c, d, e]
      output = loop ((\x -> Initial ops [x]) <$> amps) 0
  guard $ nub amps == amps
  return output

loop :: [State] -> Int -> Int
loop [a, b, c, d, e] input = case e' of
  Halted output -> output
  _ -> loop [a', b', c', d', e'] $ getOutput' e'
  where
    a' = run $ addInput a input
    b' = run . addInput b $ getOutput' a'
    c' = run . addInput c $ getOutput' b'
    d' = run . addInput d $ getOutput' c'
    e' = run . addInput e $ getOutput' d'

getOutput' :: State -> Int
getOutput' = fromJust . getOutput
