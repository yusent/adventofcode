import Control.Monad (join)
import Data.List (find)
import Data.List.Split (splitOn)
import Data.Map.Strict (Map, (!?), empty, fromList, insertWith, toList)
import Data.Maybe (isJust, fromJust)

data Object = Center (Map String Object) | Planet

main :: IO ()
main = do
  map' <- foldl add empty . lines <$> readFile "input/day06"
  let orbits = buildOrbits "COM" map'
  putStrLn $ "Part 1: " ++ show (countOrbits 0 orbits)
  putStrLn $ "Part 2: " ++ show (uncurry (+) . fromJust $ countTransfers orbits)
  where
    add acc str = let [c, p] = splitOn ")" str in insertWith (++) c [p] acc

buildOrbits :: String -> Map String [String] -> Object
buildOrbits name map' = maybe Planet build $ map' !? name
  where
    build = Center . fromList . map (\n -> (n, buildOrbits n map'))

countOrbits :: Int -> Object -> Int
countOrbits acc Planet = acc
countOrbits acc (Center map') =
  (acc +) . sum $ countOrbits (acc + 1) . snd <$> toList map'

countTransfers :: Object -> Maybe (Int, Int)
countTransfers Planet = Nothing
countTransfers c@(Center map') =
  case find isJust (countTransfers . snd <$> toList map') of
    Just x  -> x
    Nothing -> do
      distToSanCenter <- findDistToCenterOf "SAN" 0 c
      distToYouCenter <- findDistToCenterOf "YOU" 0 c
      return (distToSanCenter, distToYouCenter)

findDistToCenterOf :: String -> Int -> Object -> Maybe Int
findDistToCenterOf name acc Planet = Nothing
findDistToCenterOf name acc (Center map') =
  join . find isJust $ foo <$> toList map'
  where
    foo (k, v)
      | k == name = Just acc
      | otherwise = findDistToCenterOf name (acc + 1) v
