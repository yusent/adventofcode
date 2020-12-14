import Data.Function (on)
import Data.List (minimumBy)
import Data.List.Split (splitOn)

data Bus = Bus { busID :: Int, waitTime :: Int, remainder :: Int } deriving Show

main :: IO ()
main = do
  [timestampStr, busesStr] <- lines <$> readFile "input/day13"

  let timestamp = read timestampStr
      buses = parseBuses timestamp 0 $ splitOn "," busesStr
      nextBus = minimumBy (compare `on` waitTime) buses

  putStrLn $ "Part 1: " ++ show (busID nextBus * waitTime nextBus)
  putStrLn $ "Part 2: " ++ show (chineseRemainder buses)

parseBuses :: Int -> Int -> [String] -> [Bus]
parseBuses _ _ [] = []
parseBuses timestamp t ("x" : rest) = parseBuses timestamp (t + 1) rest
parseBuses timestamp t (busStr : rest) =
  let busID' = read busStr
   in Bus busID' ((busID' - timestamp) `mod` busID') (busID' - t `mod` busID')
        : parseBuses timestamp (t + 1) rest

chineseRemainder :: [Bus] -> Int
chineseRemainder buses = sum (map sm buses) `mod` prod
  where
    prod = product $ map busID buses
    sm bus = let p = prod `div` busID bus
              in remainder bus * fst (egcd p $ busID bus) * p

egcd :: Int -> Int -> (Int, Int)
egcd _ 0 = (1, 0)
egcd a b = (t, s - q * t)
  where
    (s, t) = egcd b r
    (q, r) = a `divMod` b
