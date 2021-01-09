import Data.List (transpose)
import Data.List.Split (splitOn)
import Data.Set (Set, empty, insert, member, size)

type Axis = [(Int, Int)]
type State = [Axis]

main :: IO ()
main = do
  initialState <- parseState <$> readFile "input/day12"
  let after1000steps = iterate (map nextStep) initialState !! 1000
  putStrLn $ "Part 1: " ++ show (energy after1000steps)
  putStrLn $ "Part 2: " ++ show (stepsUntilRepetition initialState)

parseState :: String -> State
parseState = transpose . map pm . lines
  where
    pm = flip zip (repeat 0) . map (read . drop 2) . splitOn ", " . init . tail

nextStep :: Axis -> Axis
nextStep posVels = do
  (pos, vel) <- posVels
  let vel' = (vel +) . sum $ signum . subtract pos . fst <$> posVels
  return (pos + vel', vel')

energy :: State -> Int
energy axes = sum $ moonEnergy <$> transpose axes
  where
    moonEnergy axes = sum (abs . fst <$> axes) * sum (abs . snd <$> axes)

axisStepsUntilRepetition :: Set Axis -> Axis -> Int
axisStepsUntilRepetition prev axis
  | axis `member` prev = size prev
  | otherwise = axisStepsUntilRepetition (insert axis prev) $ nextStep axis

stepsUntilRepetition :: State -> Int
stepsUntilRepetition = foldl lcm 1 . map (axisStepsUntilRepetition empty)
