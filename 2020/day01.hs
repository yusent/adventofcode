import Data.Set (Set, empty, insert, member)
import qualified Data.Map.Strict as M (Map, (!), empty, insert, member)

main :: IO ()
main = do
  expenses <- map read . lines <$> readFile "input/day01"
  putStr "Part 1: "
  print $ findPairMultiplication empty expenses
  putStr "Part 2: "
  print $ findTripleMultiplication M.empty [] expenses

findPairMultiplication :: Set Int -> [Int] -> Int
findPairMultiplication prev (x : xs)
  | (2020 - x) `member` prev = x * (2020 - x)
  | otherwise = findPairMultiplication (insert x prev) xs

findTripleMultiplication :: M.Map Int Int -> [Int] -> [Int] -> Int
findTripleMultiplication sums prev (x : xs)
  | diff `M.member` sums = x * (sums M.! diff)
  | otherwise = findTripleMultiplication updatedSums (x : prev) xs
  where
    diff = 2020 - x
    updatedSums = updateSums prev sums
    updateSums (p : ps) = updateSums ps . M.insert (x + p) (x * p)
    updateSums _ = id
