import Data.List.Split (splitOn)
import Data.Vector (Vector, (!), (//), fromList)

main :: IO ()
main = do
  ops <- fromList . map read . splitOn "," <$> readFile "input/day02"
  putStrLn . ("Part 1: " ++) . show $ execWith 12 2 ops
  putStrLn . ("Part 2: " ++) . show $ findVerbTimesNounFor ops

execWith :: Int -> Int -> Vector Int -> Int
execWith noun verb ops = exec (ops // [(1, noun), (2, verb)]) 0

exec :: Vector Int -> Int -> Int
exec ops index = case op 0 of
  1 -> exec (ops // [(op 3, op' 1 + op' 2)]) $ index + 4
  2 -> exec (ops // [(op 3, op' 1 * op' 2)]) $ index + 4
  99 -> ops ! 0
  where
    op n = ops ! (index + n)
    op' n = ops ! op n

findVerbTimesNounFor :: Vector Int -> Int
findVerbTimesNounFor ops = head
  [ 100 * noun + verb
  | noun <- [0..99]
  , verb <- [0..99]
  , execWith noun verb ops == 19690720
  ]
