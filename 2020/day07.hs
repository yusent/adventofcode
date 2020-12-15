import Data.Char (isDigit)
import Data.List.Split (splitOn)
import Data.Set as S (Set, empty, insert, member)
import Data.Map.Strict as M (Map, (!), empty, insert, member, toList)

type Bags = Map String (Map String Int)

main :: IO ()
main = do
  bags <- foldl parseLines M.empty . lines <$> readFile "input/day07"

  let bags' = filter (canContainShinyGold bags S.empty . fst) $ toList bags
      bagsInShinyGold = countBagsIn bags "shiny gold" 1

  putStrLn $ "Part 1: " ++ show (length bags')
  putStrLn $ "Part 2: " ++ show bagsInShinyGold

parseLines :: Bags -> String -> Bags
parseLines bags line = M.insert colorName (parseContents contents) bags
  where
    contents = splitOn ", " contentString
    [colorName, contentString] = splitOn " bags contain " line
    parseContents (content : rest)
      | isDigit (head content) =
        let (qty : subColorWords) = take 3 $ words content
         in M.insert (unwords subColorWords) (read qty) $ parseContents rest
      | otherwise = parseContents rest
    parseContents [] = M.empty

canContainShinyGold :: Bags -> Set String -> String -> Bool
canContainShinyGold bags visited color
  | color `S.member` visited = False
  | "shiny gold" `M.member` subColors = True
  | otherwise = any (canContainShinyGold bags (S.insert color visited) . fst)
              $ toList subColors
  where
    subColors = bags ! color

countBagsIn :: Bags -> String -> Int -> Int
countBagsIn bags color factor =
  foldl countInSubColors 0 . M.toList $ bags ! color
  where
    countInSubColors acc (sub, qty) =
      acc + factor * qty + countBagsIn bags sub (factor * qty)
