import Data.List.Split (splitOn)
import Data.Set (fromList, intersection, size, unions)

main :: IO ()
main = do
  answers <- map (map fromList . words) . splitOn "\n\n" <$> readFile "input/day6"
  let sumAnswers f = sum $ map (size . f) answers
  putStrLn . ("Part 1: " ++) . show $ sumAnswers unions
  putStrLn . ("Part 2: " ++) . show . sumAnswers $ foldl1 intersection
