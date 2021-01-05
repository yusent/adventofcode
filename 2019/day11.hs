import Data.Set (Set, delete, empty, insert, member, size)
import IntCode (Instructions, State(..), addInput, getOutput, load, reverseOutput, run)

data RobotAction = Moving | Painting
data RobotDirection = U | R | D | L

data RobotState = RobotState
  { xCoord    :: Int
  , yCoord    :: Int
  , minXCoord :: Int
  , maxXCoord :: Int
  , minYCoord :: Int
  , maxYCoord :: Int
  , action    :: RobotAction
  , whites    :: Set (Int, Int)
  , painted   :: Set (Int, Int)
  , direction :: RobotDirection
  , progState :: State
  }

main :: IO ()
main = do
  ops <- load <$> readFile "input/day11"
  putStrLn $ "Part 1: " ++ show (getTotalPainted ops)
  let (totalPainted, minX, maxX, minY, maxY, whites) = paint ops
  putStrLn "Part 2:"
  putStrLn . unlines $ draw minX maxX minY maxY whites

getTotalPainted :: Instructions -> Int
getTotalPainted ops =
  let ps = reverseOutput . run $ Initial ops []
      (t, _, _, _, _, _) = runRobot $ RobotState 0 0 0 0 0 0 Painting empty empty U ps
   in t

draw :: Int -> Int -> Int -> Int -> Set (Int, Int) -> [String]
draw minX maxX minY maxY whites = drawRow <$> [maxY, maxY - 1..minY]
  where
    drawRow y = do
      x <- [minX..maxX]
      let char = if member (x, y) whites then '#' else '.'
      return char

paint :: Instructions -> (Int, Int, Int, Int, Int, Set (Int, Int))
paint ops =
  let ps = reverseOutput . run $ Initial ops [1]
   in runRobot $ RobotState 0 0 0 0 0 0 Painting empty empty U ps

runRobot :: RobotState -> (Int, Int, Int, Int, Int, Set (Int, Int))
runRobot (RobotState _ _ minX maxX minY maxY _ w p _ (Halted [])) =
  (size p, minX, maxX, minY, maxY, w)
runRobot (RobotState x y minX maxX minY maxY a w p d ps) | null $ getOutput ps = runRobot $ RobotState x y minX maxX minY maxY a w p d ps'
  | otherwise = case (a, output, onWhite, d) of
    (Painting, 0, True, _) ->
      runAgain x y Moving (delete (x, y) w) p d

    (Painting, 1, False, _) ->
      runAgain x y Moving (insert (x, y) w) (insert (x, y) p) d

    (Painting, _, _, _) ->
      runAgain x y Moving w p d

    (Moving, 0, _, U) ->
      runAgain (x - 1) y Painting w p L

    (Moving, 0, _, R) ->
      runAgain x (y + 1) Painting w p U

    (Moving, 0, _, D) ->
      runAgain (x + 1) y Painting w p R

    (Moving, 0, _, L) ->
      runAgain x (y - 1) Painting w p D

    (Moving, 1, _, U) ->
      runAgain (x + 1) y Painting w p R

    (Moving, 1, _, R) ->
      runAgain x (y - 1) Painting w p D

    (Moving, 1, _, D) ->
      runAgain (x - 1) y Painting w p L

    (Moving, 1, _, L) ->
      runAgain x (y + 1) Painting w p U

  where
    ps' = reverseOutput . run . addInput ps $ if member (x, y) w then 1 else 0
    output = head $ getOutput ps
    onWhite = member (x, y) w
    runAgain x' y' a' w' p' d' =
      runRobot $ RobotState x' y' minX' maxX' minY' maxY' a' w' p' d' newState
      where
        minX' = min minX x'
        maxX' = max maxX x'
        minY' = min minY y'
        maxY' = max maxY y'
    newState = case ps of
      WaitingForInput i pnt rb [] (_ : res) -> WaitingForInput i pnt rb [] res
      Halted (_ : res) -> Halted res
