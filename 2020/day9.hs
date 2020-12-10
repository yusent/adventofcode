import Data.Maybe (fromJust, isJust)
import Data.List (tails, sort)

main :: IO ()
main = do
  numbers <- map read . lines <$> readFile "input/day9"
  let invalidNumber = findInvalid numbers
      weaknessSubList = sort $ findWeaknessSubList invalidNumber numbers
      weakness = head weaknessSubList + last weaknessSubList
  putStrLn $ "Part 1: " ++ show invalidNumber
  putStrLn $ "Part 2: " ++ show weakness

findInvalid :: [Int] -> Int
findInvalid numbers@(_ : next)
  | valid n prev = findInvalid next
  | otherwise = n
 where
   (prev, (n : _)) = splitAt 25 numbers

valid :: Int -> [Int] -> Bool
valid n (x : xs) = n - x `elem` xs || valid n xs
valid n _ = False

findWeaknessSubList :: Int -> [Int] -> [Int]
findWeaknessSubList invalidNumber =
  fromJust . head . filter isJust . map (sums []) . tails
  where
    sums acc@((_, accSum) : _) (x : xs)
      | accSum == invalidNumber = Just $ map fst acc
      | otherwise = sums ((x, accSum + x) : acc) xs
    sums [] (x : xs) = sums [(x, x)] xs
    sums _ _ = Nothing
