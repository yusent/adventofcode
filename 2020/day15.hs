import Data.Map.Strict (Map, (!?), fromList, insert)

main :: IO ()
main = do
  let input = [2, 1, 10, 11, 0, 6]
      mem = fromList $ zip (init input) [1..]
      numbers = 0 : init input ++ genNumList mem (length input) (last input)
      genNumList m i n = seq n
        $ n : genNumList (insert n i m) (i + 1) (maybe 0 (i -) $ m !? n)

  putStrLn . ("Part 1: " ++) . show $ numbers !! 2020
  putStrLn . ("Part 2: " ++) . show $ numbers !! 30000000
