import Control.Monad (foldM)
import Data.List.Split (splitOn)
import Data.Map.Strict (Map, (!), fromList)

data Rule = Sequence [Rule] | AnyOf Rule Rule | StartsWith Char

main :: IO ()
main = do
  [ruleStrs, strings] <- map lines . splitOn "\n\n" <$> readFile "input/day19"

  let preRules = fromList $ fmap (drop 2) . span (/= ':') <$> ruleStrs
      rule = readRule preRules "0"
      count1 = length $ filter ((== Just "") . obeysRule rule) strings

  putStrLn $ "Part 1: " ++ show count1

readRule :: Map String String -> String -> Rule
readRule preRules id = case splitOn "|" (preRules ! id) of
  ['"' : char : _] -> StartsWith char
  [idsBody] -> readSeqRule idsBody
  [body1, body2] -> AnyOf (readSeqRule body1) (readSeqRule body2)
  where
    readSeqRule = Sequence . map (readRule preRules) . words

obeysRule :: Rule -> String -> Maybe String
obeysRule (StartsWith char) (c : rest) = if char == c then Just rest else Nothing
obeysRule (Sequence rules) string = foldM (\s r -> obeysRule r s) string rules
obeysRule (AnyOf r1 r2) str = maybe (obeysRule r2 str) Just $ obeysRule r1 str
