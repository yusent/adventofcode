import Data.Char (isDigit, isHexDigit)

main :: IO ()
main = do
  (c1, c2) <- countValid . parsePassports <$> readFile "day4-input"

  putStrLn $ "Part 1: " ++ show c1
  putStrLn $ "Part 2: " ++ show c2

parsePassports :: String -> [[(String, String)]]
parsePassports contents = case span (/= '\n') contents of
  (section, '\n' : '\n' : rest) -> parsePassport section : parsePassports rest
  (partial, '\n' : rest)        -> parsePassports $ partial ++ (' ' : rest)
  (final, _)                    -> [parsePassport final]
  where
    parsePassport = foldl inserKeyVal [] . words
    inserKeyVal m str =
      let (key, ':' : val) = span (/= ':') str
       in (key, val) : m

countValid :: [[(String, String)]] -> (Int, Int)
countValid = foldl count (0, 0)
  where
    count (c1, c2) p
      | check1 p = (c1 + 1, c2 + if check2 p then 1 else 0)
      | otherwise = (c1, c2)
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    check1 p = all (`elem` (fst <$> p)) required
    check2 = all (uncurry valid)

valid :: String -> String -> Bool
valid "byr" = inRange 1920 2002
valid "iyr" = inRange 2010 2020
valid "eyr" = inRange 2020 2030
valid "hgt" = uncurry (flip validHeight) . span isDigit
valid "hcl" = \(h : t) -> h == '#' && map isHexDigit t == replicate 6 True
valid "ecl" = flip elem ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid "pid" = (== replicate 9 True) . map isDigit
valid _ = const True

inRange :: Int -> Int -> String -> Bool
inRange a b = (\x -> x >= a && x <= b) . read

validHeight :: String -> String -> Bool
validHeight "cm" = inRange 150 193
validHeight "in" = inRange 59 76
validHeight _ = const False
