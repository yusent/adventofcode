import Data.List.Split
import Data.Map.Strict (alter, empty)
import Data.Maybe

main = do
  lines' <- map parseLine . lines <$> readFile "input/day05"
  let points = foldl getPoints empty $ filter isOrthogonal lines'
      points' = foldl getPoints points $ filter isDiagonal lines'
  putStrLn $ "Part 1: " ++ show (countOverlaps points)
  putStrLn $ "Part 2: " ++ show (countOverlaps points')

parseLine = map (map read . splitOn ",") . splitOn " -> "

getPoints acc [[x, y], [x', y']]
  | x == x' && y == y' = acc'
  | x == x' = getPoints acc' [[x, y''], [x', y']]
  | y == y' = getPoints acc' [[x'', y], [x', y']]
  | otherwise = getPoints acc' [[x'', y''], [x', y']]
  where
    acc' = alter (\c -> Just $ fromMaybe 0 c + 1) (x, y) acc
    x'' = x + if x > x' then -1 else 1
    y'' = y + if y > y' then -1 else 1

isOrthogonal [[x, y], [x', y']] = x == x' || y == y'

isDiagonal [[x, y], [x', y']] = abs (x - x') == abs (y - y')

countOverlaps = foldl (\acc c -> acc + if c > 1 then 1 else 0) 0
