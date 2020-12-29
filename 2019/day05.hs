import Data.List.Split (splitOn)
import Data.Vector (Vector, (!), (//), fromList)

main :: IO ()
main = do
  ops <- fromList . map read . splitOn "," <$> readFile "input/day05"
  putStrLn . ("Part 1: " ++) . show . head $ exec ops 1 [] 0
  putStrLn . ("Part 2: " ++) . show . head $ exec ops 5 [] 0

exec :: Vector Int -> Int -> [Int] -> Int -> [Int]
exec ops input output index = case opCode of
  1 -> exec (storeAt 3 $ op' 1 + op' 2) input output $ index + 4
  2 -> exec (storeAt 3 $ op' 1 * op' 2) input output $ index + 4
  3 -> exec (storeAt 1 input) input output $ index + 2
  4 -> exec ops input (op' 1 : output) $ index + 2
  5 -> exec ops input output $ if op' 1 /= 0 then op' 2 else index + 3
  6 -> exec ops input output $ if op' 1 == 0 then op' 2 else index + 3
  7 -> exec (storeAt 3 $ if op' 1 < op' 2 then 1 else 0) input output $ index + 4
  8 -> exec (storeAt 3 $ if op' 1 == op' 2 then 1 else 0) input output $ index + 4
  99 -> output
  where
    (mode, opCode) = op 0 `divMod` 100
    op n = ops ! (index + n)
    op' n = if modes !! (n - 1) == 0 then ops ! op n else op n
    modes = modes' mode
    modes' m = let (d, r) = m `divMod` 10 in r : modes' d
    storeAt addressOp value = ops // [(op addressOp, value)]
