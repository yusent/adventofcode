import Control.Monad (mapM_)
import Data.List (minimumBy)
import Data.List.Split (chunksOf)

main :: IO ()
main = do
  pixels <- init <$> readFile "input/day08"
  let width = 25
      height = 6
      layers = chunksOf (width * height) pixels
      layer = minimumBy (\l l' -> compare (freq '0' l) (freq '0' l')) layers
      freq char = length . filter (== char)
      visual '0' = '.'
      visual '1' = '#'
  putStrLn $ "Part 1: " ++ show (freq '1' layer * freq '2' layer)
  putStrLn "Part 2:"
  mapM_ putStrLn . chunksOf width $ visual <$> foldl1 placeBehind layers

placeBehind :: String -> String -> String
placeBehind ('2' : xs) (y : ys) = y : placeBehind xs ys
placeBehind (x : xs) (_ : ys) = x : placeBehind xs ys
placeBehind _ _ = []
