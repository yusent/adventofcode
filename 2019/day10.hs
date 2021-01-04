import Control.Monad (guard)
import Data.Array.BitArray (BitArray, (!), (!?), (//), listArray)
import Data.List (maximumBy, nub, sort)
import Data.Maybe (isJust)
import Data.Ratio ((%), denominator, numerator)

type Map = BitArray (Int, Int)

main :: IO ()
main = do
  rows <- lines <$> readFile "input/day10"
  let height = length rows
      width = length $ head rows
      slopes' = slopes height width
      map' = listArray ((1, 1), (height, width)) $ (== '#') <$> concat rows
      (y, x, asteroidsCount) = bestPlace map' slopes' height width
      (y', x') = findDestroyedAsteroid 200 map' slopes' slopes' y x
  putStrLn $ "Part 1: " ++ show asteroidsCount
  putStrLn $ "Part 2: " ++ show ((x' - 1) * 100 + y' - 1)

findDestroyedAsteroid
  :: Int -> Map -> [(Int, Int)] -> [(Int, Int)] -> Int -> Int -> (Int, Int)
findDestroyedAsteroid n map' origSlopes [] y x =
  findDestroyedAsteroid n map' origSlopes origSlopes y x
findDestroyedAsteroid n map' origSlopes ((offY, offX) : slopes') y x =
  case findAsteroid map' y x offY offX of
    Just (y', x') ->
      if n == 1
         then (y', x')
         else let map'' = map' // [((y', x'), False)]
               in findDestroyedAsteroid (n - 1) map'' origSlopes slopes' y x
    Nothing -> findDestroyedAsteroid n map' origSlopes slopes' y x

bestPlace :: Map -> [(Int, Int)] -> Int -> Int -> (Int, Int, Int)
bestPlace map' slopes' height width =
  maximumBy (\(_, _, a) (_, _, b) -> compare a b) $ do
    y <- [1..height]
    x <- [1..width]
    guard $ map' ! (y, x)
    return (y, x, countAsteroids map' 0 slopes' height width y x)

countAsteroids :: Map -> Int -> [(Int, Int)] -> Int -> Int -> Int -> Int -> Int
countAsteroids _ acc [] _ _ _ _ = acc
countAsteroids map' acc ((offY, offX) : slopes') height width y x =
  countAsteroids map' (acc + accInc) slopes' height width y x
  where
    accInc = if isJust (findAsteroid map' y x offY offX) then 1 else 0

findAsteroid :: Map -> Int -> Int -> Int -> Int -> Maybe (Int, Int)
findAsteroid map' y x offsetY offsetX = case map' !? (y', x') of
  Just True  -> Just (y', x')
  Just False -> findAsteroid map' y' x' offsetY offsetX
  Nothing    -> Nothing
  where
    y' = y + offsetY
    x' = x + offsetX

slopes :: Int -> Int -> [(Int, Int)]
slopes height width =
  (-1, 0) : slopes1q ++ (0, 1) : slopes2q ++ (1, 0) : slopes3q ++ (0, -1) : slopes4q
  where
    slopes1q = (\r -> (- denominator r, numerator r)) <$> absSlopes
    slopes2q = (\r -> (denominator r, numerator r)) <$> reverse absSlopes
    slopes3q = (\r -> (denominator r, - numerator r)) <$> absSlopes
    slopes4q = (\r -> (- denominator r, - numerator r)) <$> reverse absSlopes
    absSlopes = sort . nub $ do
      offX <- [1..width]
      offY <- [1..height]
      return $ offX % offY
