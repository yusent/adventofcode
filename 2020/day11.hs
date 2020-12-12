import Data.Vector (Vector, (!), fromList, toList)

type Layout = Vector (Int, Vector (Int, Char))

main :: IO ()
main = do
  layout <- makeVector . map makeVector . lines <$> readFile "input/day11"
  print $ count False layout
  print $ count True layout
  where
    makeVector = fromList . zip [0..]

count :: Bool -> Layout -> Int
count rule2 layout
  | layout == nextLayout = sum . map (length . filter (== '#') . makeList) $ makeList layout
  | otherwise = count rule2 nextLayout
  where
    nextLayout = nextRound rule2 layout
    makeList = map snd . toList

nextRound :: Bool -> Layout -> Layout
nextRound rule2 layout = calcRow <$> layout
  where
    calcRow (y, row) = (y, calcCell y <$> row)
    calcCell y (x, cell)
      | cell == 'L' && neighboursCount == 0 = (x, '#')
      | cell == '#' && neighboursCount >= seatsLimit = (x, 'L')
      | otherwise = (x, cell)
      where
        neighboursCount = countNeighbours layout x y rule2
        seatsLimit = if rule2 then 5 else 4

countNeighbours :: Layout -> Int -> Int -> Bool -> Int
countNeighbours layout x y rule2 = sum
  [ findSeat layout x y offX offY rule2
  | offX <- [-1..1]
  , offY <- [-1..1]
  , not (offX == 0 && offY == 0)
  ]

findSeat :: Layout -> Int -> Int -> Int -> Int -> Bool -> Int
findSeat layout x y offX offY rule2
  | y' < 0 || y' >= length layout = 0
  | x' < 0 || x' >= length (snd $ layout ! y') = 0
  | cell == '#' = 1
  | cell == '.' && rule2 = findSeat layout x' y' offX offY rule2
  | otherwise = 0
  where
    x' = x + offX
    y' = y + offY
    cell = snd $ snd (layout ! y') ! x'
