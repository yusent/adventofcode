import Control.Monad (guard)
import Data.List (group)

main :: IO ()
main = do
  let (from, to) = (231832, 767346) -- Input
  putStrLn . ("Part 1: " ++) . show . length $ validPasswords False from to
  putStrLn . ("Part 2: " ++) . show . length $ validPasswords True from to

validPasswords :: Bool -> Int -> Int -> [Int]
validPasswords part2 from to = do
  a <- [1..9]
  b <- [a..9]
  c <- [b..9]
  d <- [c..9]
  e <- [d..9]
  f <- [e..9]
  let n = 100000 * a + 10000 * b + 1000 * c + 100 * d + 10 * e + f
  guard $ if part2
             then any ((==2) . length) $ group [a, b, c, d, e, f]
             else a == b || b == c || c == d || d == e || e == f
  guard $ n >= from && n <= to
  return n
