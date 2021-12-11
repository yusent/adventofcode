import qualified Data.Map as M
import qualified Data.Set as S
import Data.List
import Data.List.Split

main = do
  lns <- lines <$> readFile "input/day08"
  let codes = map (map S.fromList . words) . splitOn " | " <$> lns
  putStrLn $ "Part 1: " ++ show (countEasyDigits $ last <$> codes)
  putStrLn $ "Part 2: " ++ show (sum $ decodeOutput <$> codes)

countEasyDigits = sum . map (length . filter ((`elem` [2, 3, 4, 7]) . S.size))

decodeOutput :: [[S.Set Char]] -> Int
decodeOutput [xs, ys] =
  let ss = xs ++ ys
      ds0 = foldl decode M.empty ss
      ds1 = foldl decode' ds0 ss
      ds2 = foldl decode'' ds1 ss
      ds3 = foldl decode''' ds2 ss
      ds = foldl (\acc (k, v) -> M.insert v k acc) M.empty $ M.toList ds3
   in read . concat $ (show . (ds M.!)) <$> ys

decode ds s
  | S.size s == 2 = M.insert 1 s ds
  | S.size s == 4 = M.insert 4 s ds
  | S.size s == 3 = M.insert 7 s ds
  | S.size s == 7 = M.insert 8 s ds
  | otherwise = ds

decode' ds s
  | S.size s == 5 && S.size (S.intersection s d4) == 2 = M.insert 2 s ds
  | S.size s == 5 && S.intersection s d7 == d7 = M.insert 3 s ds
  | S.size s == 6 && S.intersection s d4 == d4 = M.insert 9 s ds
  | otherwise = ds
  where
    d4 = ds M.! 4
    d7 = ds M.! 7

decode'' ds s
  | S.size s == 5 && s /= (ds M.! 2) && s/= (ds M.! 3) = M.insert 5 s ds
  | S.size s == 6 && S.intersection s d7 == d7 && s/= (ds M.! 9) = M.insert 0 s ds
  | otherwise = ds
  where
    d7 = ds M.! 7

decode''' ds s
  | S.size s == 6 && s /= (ds M.! 0) && s/= (ds M.! 9) = M.insert 6 s ds
  | otherwise = ds
