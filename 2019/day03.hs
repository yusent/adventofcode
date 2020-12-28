import Data.List.Split (splitOn)

type Coord = (Int, Int)

main :: IO ()
main = do
  [p1, p2] <- map readCoords . lines <$> readFile "input/day03"
  let (_, _, _, intersections) = foldl (solve p2) (0, 0, 0, []) p1
  putStrLn . ("Part 1: " ++) . show . minimum $ fst <$> intersections
  putStrLn . ("Part 2: " ++) . show . minimum $ snd <$> init intersections

solve :: [Coord] -> (Int, Int, Int, [Coord]) -> Coord -> (Int, Int, Int, [Coord])
solve p2 (prevX, prevY, steps, intersections) (x, y) =
  (x, y, steps + abs (x - prevX) + abs (y - prevY), updatedIntersections)
  where
    minX = min prevX x
    maxX = max prevX x
    minY = min prevY y
    maxY = max prevY y
    (_, _, _, updatedIntersections) = foldl solve' (0, 0, 0, intersections) p2
    solve' (prevX', prevY', steps', intersections') (x', y')
      | minX <= maxX' && minX' <= maxX && minY <= maxY' && minY' <= maxY =
        (x', y', steps'', intersection : intersections')
      | otherwise = (x', y', steps'', intersections')
      where
        minX' = min prevX' x'
        minY' = min prevY' y'
        maxX' = max prevX' x'
        maxY' = max prevY' y'
        steps'' = steps' + abs (x' - prevX') + abs (y' - prevY')
        intersection = (abs ix + abs iy, steps + steps' + stepsToI)
        (ix, iy, stepsToI)
          | prevX == x = (x, y', abs (x - prevX') + abs (y' - prevY))
          | otherwise = (x', y, abs (x' - prevX) + abs (y - prevY'))

readCoords :: String -> [(Int, Int)]
readCoords = tail . reverse . foldl move [(0, 0)] . splitOn ","

move :: [Coord] -> String -> [Coord]
move coords@((x, y) : _) moveStr = move' x y moveStr : coords
  where
    move' x y ('U' : stepsStr) = (x, y + read stepsStr)
    move' x y ('D' : stepsStr) = (x, y - read stepsStr)
    move' x y ('R' : stepsStr) = (x + read stepsStr, y)
    move' x y ('L' : stepsStr) = (x - read stepsStr, y)
