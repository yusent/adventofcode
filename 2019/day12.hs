import Control.Monad (mapM_)
import Data.List.Split (splitOn)
import Data.Set (Set, empty, insert, member)

data Vector = Vector { x :: Int, y :: Int, z :: Int } deriving (Eq, Ord)
data Moon = Moon { pos :: Vector, vel :: Vector } deriving (Eq, Ord)

main :: IO ()
main = do
  moons <- map parseMoon . lines <$> readFile "input/day12"
  let after1000steps = foldl (\acc _ -> nextStep acc) moons [1..1000]
  putStrLn $ "Part 1: " ++ show (sum $ energy <$> after1000steps)
  putStrLn $ "Part 2: " ++ show (stepsUntilRepetition empty 0 moons)

parseMoon :: String -> Moon
parseMoon = buildMoon . map (read . drop 2) . splitOn ", " . init . tail
  where
    buildMoon [x, y, z] = Moon (Vector x y z) $ Vector 0 0 0

nextStep :: [Moon] -> [Moon]
nextStep moons = applyGravity . updateVelocity <$> moons
  where
    applyGravity (Moon p v) = Moon (add p v) v
    updateVelocity (Moon p v) = Moon p . foldl add v $ offsets p . pos <$> moons

add :: Vector -> Vector -> Vector
add (Vector x y z) (Vector x' y' z') = Vector (x + x') (y + y') (z + z')

offsets :: Vector -> Vector -> Vector
offsets (Vector x y z) (Vector x' y' z') =
  Vector (cmp x x') (cmp y y') (cmp z z')
  where
    cmp a b
      | a < b = 1
      | a > b = -1
      | otherwise = 0

energy :: Moon -> Int
energy (Moon (Vector x y z) (Vector x' y' z')) = potential * kinetic
  where
    potential = abs x + abs y + abs z
    kinetic = abs x' + abs y' + abs z'

stepsUntilRepetition :: Set [Moon] -> Int -> [Moon] -> Int
stepsUntilRepetition prevStates steps moons
  | moons `member` prevStates = steps
  | otherwise = stepsUntilRepetition (insert moons prevStates) (steps + 1)
              $ nextStep moons

printMoon :: Moon -> IO ()
printMoon (Moon (Vector x y z) (Vector x' y' z')) = do
  putStrLn $ "pos=<x=" ++ show x ++ ",y=" ++ show y ++ ",z=" ++ show z ++ ">, vel=<x=" ++ show x' ++ ",y=" ++ show y' ++ ",z=" ++ show z' ++ ">"
