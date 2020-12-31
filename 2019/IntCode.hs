module IntCode
  ( State(..)
  , addInput
  , execUntilHalt
  , getOutput
  , run
  ) where

import Data.Maybe (fromMaybe)
import Data.Vector (Vector, (!), (//), fromList)

type Instructions = Vector Int
type Pointer = Int
type Input = [Int]
type Output = Maybe Int
data State = Initial Instructions Input
           | WaitingForInput Instructions Pointer Input Output
           | Halted Int

addInput :: State -> Int -> State
addInput (Initial ops input) x = Initial ops (input ++ [x])
addInput (WaitingForInput ops index input output) x =
  WaitingForInput ops index (input ++ [x]) output

getOutput :: State -> Output
getOutput (WaitingForInput _ _ _ output) = output
getOutput (Halted output) = Just output

run :: State -> State
run (Initial ops input) = exec ops input Nothing 0
run (WaitingForInput ops index input@(_ : _) _) = exec ops input Nothing index
run state = state

exec :: Instructions -> Input -> Output -> Pointer -> State
exec ops input output index = case opCode of
  1 -> exec (storeAt 3 $ op' 1 + op' 2) input output $ index + 4
  2 -> exec (storeAt 3 $ op' 1 * op' 2) input output $ index + 4
  3 -> if null input
          then WaitingForInput ops index [] output
          else exec (storeAt 1 $ head input) (tail input) output $ index + 2
  4 -> exec ops input (Just $ op' 1) $ index + 2
  5 -> exec ops input output $ if op' 1 /= 0 then op' 2 else index + 3
  6 -> exec ops input output $ if op' 1 == 0 then op' 2 else index + 3
  7 -> exec (storeAt 3 $ if op' 1 < op' 2 then 1 else 0) input output $ index + 4
  8 -> exec (storeAt 3 $ if op' 1 == op' 2 then 1 else 0) input output $ index + 4
  99 -> Halted $ fromMaybe (ops ! 0) output
  where
    (mode, opCode) = op 0 `divMod` 100
    op n = ops ! (index + n)
    op' n = if modes !! (n - 1) == 0 then ops ! op n else op n
    modes = modes' mode
    modes' m = let (d, r) = m `divMod` 10 in r : modes' d
    storeAt addressOp value = ops // [(op addressOp, value)]

execUntilHalt :: Instructions -> Input -> Int
execUntilHalt ops input = case run (Initial ops input) of
  Halted output -> output
  _ -> error "Not enough input"
