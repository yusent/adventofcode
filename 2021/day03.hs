import Data.List

main = do
  binNums <- lines <$> readFile "input/day03"
  putStrLn $ "Part 1: " ++ show (powerConsumption binNums)
  putStrLn $ "Part 2: " ++ show (lifeSupportRating binNums)

powerConsumption = powerConsumption' . map mostCommonBit . transpose

lifeSupportRating ns = lfRating (==) 0 ns * lfRating (/=) 0 ns

powerConsumption' gammaRate = binToDec '1' gammaRate * binToDec '0' gammaRate

lfRating _ _ [num] = binToDec '1' num
lfRating f i nums = lfRating f (i + 1) $ filter (f mcb . (!! i)) nums
  where mcb = mostCommonBit $ (!! i) <$> nums

mostCommonBit xs
  | 2 * length (filter (== '1') xs) >= length xs = '1'
  | otherwise = '0'

binToDec oneChar = sum . map (2^) . findIndices (== oneChar) . reverse
