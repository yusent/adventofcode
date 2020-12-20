import qualified Data.Map.Strict as M (Map, alter, foldlWithKey, empty)
import Data.Set (Set, delete, empty, insert, member, notMember, size)

main :: IO ()
main = do
  tiles <- map (readTile (0, 0)) . lines <$> readFile "input/day24"
  let blackTiles = foldl flipTile empty tiles
      blackTilesAfter100Days = foldl (\acc _ -> nextDay acc) blackTiles [1..100]
  putStrLn $ "Part 1: " ++ show (size blackTiles)
  putStrLn $ "Part 2: " ++ show (size blackTilesAfter100Days)

readTile :: (Int, Int) -> String -> (Int, Int)
readTile (x, y) ('n' : 'e' : rest) = readTile (x, y + 1) rest
readTile (x, y) ('n' : 'w' : rest) = readTile (x - 1, y + 1) rest
readTile (x, y) ('s' : 'e' : rest) = readTile (x + 1, y - 1) rest
readTile (x, y) ('s' : 'w' : rest) = readTile (x, y - 1) rest
readTile (x, y) ('e' : rest) = readTile (x + 1, y) rest
readTile (x, y) ('w' : rest) = readTile (x - 1, y) rest
readTile (x, y) [] = (x, y)

flipTile :: Set (Int, Int) -> (Int, Int) -> Set (Int, Int)
flipTile blackTiles tile
  | tile `member` blackTiles = delete tile blackTiles
  | otherwise = insert tile blackTiles

nextDay :: Set (Int, Int) -> Set (Int, Int)
nextDay blackTiles = M.foldlWithKey update empty counts
  where
    update acc c count
      | c `member` blackTiles && (count == 1 || count == 2) = insert c acc
      | c `notMember` blackTiles && count == 2 = insert c acc
      | otherwise = acc
    counts = foldl incNeighbours M.empty blackTiles

incNeighbours :: M.Map (Int, Int) Int -> (Int, Int) -> M.Map (Int, Int) Int
incNeighbours counts (x, y) =
  foldl inc counts [(0, 1), (-1, 1), (1, -1), (0, -1), (1, 0), (-1, 0)]
  where
    inc acc (x', y') = M.alter inc' (x + x', y + y') acc
    inc' (Just k) = Just $ k + 1
    inc' Nothing = Just 1
