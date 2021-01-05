module IntCode
  ( Instructions
  , State(..)
  , addInput
  , execUntilHalt
  , getOutput
  , load
  , reverseOutput
  , run
  ) where

import Data.List.Split (splitOn)
import Data.Maybe (fromMaybe)
import Data.Map.Strict (Map, findWithDefault, fromList, insert)

type Instructions = Map Int Int
type Pointer = Int
type Input = [Int]
type Output = [Int]
data State = Initial Instructions Input
           | WaitingForInput Instructions Pointer Int Input Output
           | Halted Output

load :: String -> Instructions
load = fromList . zip [0..] . map read . splitOn ","

addInput :: State -> Int -> State
addInput (Initial ops input) x = Initial ops (input ++ [x])
addInput (WaitingForInput ops index rBase input output) x =
  WaitingForInput ops index rBase (input ++ [x]) output
addInput (Halted output) _ = Halted output

getOutput :: State -> Output
getOutput (WaitingForInput _ _ _ _ output) = output
getOutput (Halted output) = output

reverseOutput :: State -> State
reverseOutput (WaitingForInput ins pnt idx input output) =
  WaitingForInput ins pnt idx input $ reverse output
reverseOutput (Halted output) = Halted $ reverse output

run :: State -> State
run (Initial ops input) = exec ops input [] 0 0
run (WaitingForInput ops index rBase input@(_ : _) _) = exec ops input [] rBase index
run state = state

exec :: Instructions -> Input -> Output -> Int -> Pointer -> State
exec ops input output rBase index = case opCode of
  1 -> exec (storeAt 3 $ op' 1 + op' 2) input output rBase $ index + 4
  2 -> exec (storeAt 3 $ op' 1 * op' 2) input output rBase $ index + 4
  3 -> if null input
          then WaitingForInput ops index rBase [] output
          else exec (storeAt 1 $ head input) (tail input) output rBase $ index + 2
  4 -> exec ops input (op' 1 : output) rBase $ index + 2
  5 -> exec ops input output rBase $ if op' 1 /= 0 then op' 2 else index + 3
  6 -> exec ops input output rBase $ if op' 1 == 0 then op' 2 else index + 3
  7 -> exec (storeAt 3 $ if op' 1 < op' 2 then 1 else 0) input output rBase $ index + 4
  8 -> exec (storeAt 3 $ if op' 1 == op' 2 then 1 else 0) input output rBase $ index + 4
  9 -> exec ops input output (rBase + op' 1) $ index + 2
  99 -> Halted $ if null output then [findWithDefault 0 0 ops] else output
  unknown -> error $ "Unknown op code: " ++ show unknown
  where
    (mode, opCode) = op 0 `divMod` 100
    op n = findWithDefault 0 (index + n) ops
    op' n =
      case modes !! (n - 1) of
        0 -> findWithDefault 0 (op n) ops
        1 -> op n
        2 -> findWithDefault 0 (op n + rBase) ops
    modes = modes' mode
    modes' m = let (d, r) = m `divMod` 10 in r : modes' d
    storeAt addressOp value =
      let mode' = modes !! fromIntegral (addressOp - 1)
          offset = if mode' == 2 then rBase else 0
       in insert (op addressOp + offset) value ops

execUntilHalt :: Instructions -> Input -> Int
execUntilHalt ops input = case run (Initial ops input) of
  Halted (output : _) -> output
  _ -> error "Not enough input"
