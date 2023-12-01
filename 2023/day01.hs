import Data.Char (isDigit)

main = do
  calibrationData <- lines <$> readFile "input/day01"
  putStrLn $ ("Part 1: " ++) . show . sum $ calibrationValue . filter isDigit <$> calibrationData
  putStrLn $ ("Part 2: " ++) . show . sum $ calibrationValue . wordsToDigits <$> calibrationData

calibrationValue digits = read [head digits, last digits]

wordsToDigits "" = []
wordsToDigits ('o' : 'n' : rest@('e' : _)) = '1' : wordsToDigits rest
wordsToDigits ('t' : 'w' : rest@('o' : _)) = '2' : wordsToDigits rest
wordsToDigits ('t' : 'h' : 'r' : 'e' : rest@('e' : _)) = '3' : wordsToDigits rest
wordsToDigits ('f' : 'o' : 'u' : 'r' : rest) = '4' : wordsToDigits rest
wordsToDigits ('f' : 'i' : 'v' : rest@('e' : _)) = '5' : wordsToDigits rest
wordsToDigits ('s' : 'i' : 'x' : rest) = '6' : wordsToDigits rest
wordsToDigits ('s' : 'e' : 'v' : 'e' : rest@('n' : _)) = '7' : wordsToDigits rest
wordsToDigits ('e' : 'i' : 'g' : 'h' : rest@('t' : _)) = '8' : wordsToDigits rest
wordsToDigits ('n' : 'i' : 'n' : rest@('e' : _)) = '9' : wordsToDigits rest
wordsToDigits (d : rest) = if isDigit d then (d : wordsToDigits rest) else wordsToDigits rest
