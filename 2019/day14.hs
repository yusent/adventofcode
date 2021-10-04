import Data.List.Split (splitOn)
import Data.Map.Strict (Map, (!), empty, findWithDefault, insert)

type Ingredient = (Int, String)
type Reactions = Map String (Int, [Ingredient])

main :: IO ()
main = do
  reactions <- parseReactions <$> readFile "input/day14"
  let (_, orePerFuel) = react reactions (empty, 0) (1, "FUEL")
      minFuelWithTrillionOre = div 1000000000000 orePerFuel
      (waste, ore) = react reactions (empty, 0) (minFuelWithTrillionOre, "FUEL")
  print orePerFuel
  print $ maxFuel reactions waste (1000000000000 - ore) minFuelWithTrillionOre

parseReactions :: String -> Reactions
parseReactions = foldl addReaction empty . lines
  where
    addReaction acc line = insert name (qty, ingredients) acc
      where
        [ingredientsStr, result] = splitOn " => " line
        (qty, name) = parseComponent result
        ingredients = parseComponent <$> splitOn ", " ingredientsStr

parseComponent :: String -> Ingredient
parseComponent str = let [qty, name] = words str in (read qty, name)

react :: Reactions -> (Map String Int, Int) -> Ingredient -> (Map String Int, Int)
react reactions (waste, oreAcc) (0, _) = (waste, oreAcc)
react reactions (waste, oreAcc) (qtyNeeded, "ORE") = (waste, oreAcc + qtyNeeded)
react reactions (waste, oreAcc) (qtyNeeded, name)
  | prevWaste >= qtyNeeded = (insert name (prevWaste - qtyNeeded) waste, oreAcc)
  | otherwise = (insert name (qty * factor - qtyNeeded') waste', oreAcc + oreAcc')
  where
    prevWaste = findWithDefault 0 name waste
    (qty, ingredients) = reactions ! name
    factor = ceiling $ fromIntegral qtyNeeded' / fromIntegral qty
    qtyNeeded' = qtyNeeded - prevWaste
    (waste', oreAcc') = foldl (react reactions) (waste, 0)
                      $ (\(q, n) -> (q * factor, n)) <$> ingredients

maxFuel :: Reactions -> Map String Int -> Int -> Int -> Int
maxFuel reactions waste ore fuel
  | ore > oreNeeded = maxFuel reactions waste' (ore - oreNeeded) $ fuel + 1
  | otherwise = fuel
  where
    (waste', oreNeeded) = react reactions (waste, 0) (1, "FUEL")
