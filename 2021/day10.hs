import Data.List

main = do
  scores <- map (score []) . lines <$> readFile "input/day10"
  putStrLn $ "Part 1: " ++ show (sum . map abs $ filter (<0) scores)
  let acScores = sort $ filter (>0) scores
   in putStrLn $ "Part 2: " ++ show (acScores !! (length acScores `div` 2))

score openBrackets ('(' : cs) = score ('(' : openBrackets) cs
score openBrackets ('[' : cs) = score ('[' : openBrackets) cs
score openBrackets ('{' : cs) = score ('{' : openBrackets) cs
score openBrackets ('<' : cs) = score ('<' : openBrackets) cs
score ('(' : openBrackets) (')' : cs) = score openBrackets cs
score ('[' : openBrackets) (']' : cs) = score openBrackets cs
score ('{' : openBrackets) ('}' : cs) = score openBrackets cs
score ('<' : openBrackets) ('>' : cs) = score openBrackets cs
score _ (')' : _) = -3
score _ (']' : _) = -57
score _ ('}' : _) = -1197
score _ ('>' : _) = -25137
score openBrackets [] = foldl autocompleteScore 0 openBrackets

autocompleteScore acc '(' = acc * 5 + 1
autocompleteScore acc '[' = acc * 5 + 2
autocompleteScore acc '{' = acc * 5 + 3
autocompleteScore acc '<' = acc * 5 + 4
