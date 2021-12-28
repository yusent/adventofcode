import Data.Char (intToDigit)
import Data.List (splitAt)
import Numeric (readHex, showIntAtBase)

data Packet = Literal Int Int | Operator Int Int [Packet]

main = do
  transmission <- hexToBin . head . words <$> readFile "input/day16"
  let (packet, _) = parse transmission
  putStrLn $ "Part 1: " ++ show (sumVersions packet)
  putStrLn $ "Part 2: " ++ show (pkVal packet)

sumVersions (Literal v _) = v
sumVersions (Operator v _ ps) = v + sum (sumVersions <$> ps)

pkVersion (Literal version _) = version
pkVersion (Operator version _ _) = version

pkVal (Literal _ val) = val
pkVal (Operator _ 0 ps) = sum $ pkVal <$> ps
pkVal (Operator _ 1 ps) = product $ pkVal <$> ps
pkVal (Operator _ 2 ps) = minimum $ pkVal <$> ps
pkVal (Operator _ 3 ps) = maximum $ pkVal <$> ps
pkVal (Operator _ 5 [p, q]) = fromEnum $ pkVal p > pkVal q
pkVal (Operator _ 6 [p, q]) = fromEnum $ pkVal p < pkVal q
pkVal (Operator _ 7 [p, q]) = fromEnum $ pkVal p == pkVal q

-- Parser

parse (v0 : v1: v2 : t0 : t1 : t2 : bs) = case readBin [t0, t1, t2] of
  4 -> let (val, r) = parseLiteral bs in (Literal version val, r)
  t -> let (ps, r) = parseSubPackets bs in (Operator version t ps, r)
  where version = readBin [v0, v1, v2]

parseLiteral bs = (readBin bin, rest)
  where
    (bin, rest) = extractData bs
    extractData (a : b : c : d : e : r)
      | a == '0' = ([b, c, d, e], r)
      | otherwise = let (v, r') = extractData r in (b : c : d : e : v, r')

parseSubPackets ('0' : bs) =
  let (bs'', r) = splitAt (readBin lenBin) bs' in (parsePackets bs'', r)
  where (lenBin, bs') = splitAt 15 bs
parseSubPackets ('1' : bs) =
  let (lenBin, bs') = splitAt 11 bs in parseNPackets (readBin lenBin) bs'

parsePackets [] = []
parsePackets bs = let (p, r) = parse bs in p : parsePackets r

parseNPackets 0 bs = ([], bs)
parseNPackets n bs = (p : ps, r)
  where
    (ps, r) = parseNPackets (n - 1) r'
    (p, r') = parse bs

-- Base conversion

readBin = readBin' 0 . reverse
  where
    readBin' i (b : bs) = readBin' (i + 1) bs + if b == '1' then 2 ^ i else 0
    readBin' _ [] = 0

hexToBin [] = []
hexToBin (d : ds) = zfill (showBin $ readHex [d]) ++ hexToBin ds
  where
    showBin [(bs, _)] = showIntAtBase 2 intToDigit bs ""
    zfill bs = replicate (4 - length bs) '0' ++ bs
