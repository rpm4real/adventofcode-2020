import Data.List.Split (splitOn)

checkChars :: String -> Char -> Int 
checkChars s c = length $ filter (== c) s 

findOccur :: String -> Bool
findOccur theString = 
    let (remain:password:_) = splitOn ": " theString
        (theCount:theChar:_) = splitOn " " remain 
        (low:high:_) = map read $ splitOn "-" theCount
    in checkChars password (head theChar) `elem` [low..high]

getIndex :: String -> (Int, Int) -> (Char, Char)
getIndex s (first, second) = 
    let id1 = s !! (first - 1) 
        id2 = s !! (second - 1)
    in (id1, id2)

checkPositions :: String -> Char -> (Int, Int) -> Bool
checkPositions password theChar (low, high) = 
    let (val1, val2) = getIndex password (low, high)
    in (val1 == theChar) /= (val2 == theChar)

findOccur2 :: String -> Bool
findOccur2 theString = 
    let (remain:password:_) = splitOn ": " theString
        (theCount:theChar:_) = splitOn " " remain 
        (first:second:_) = map read $ splitOn "-" theCount
    in checkPositions password (head theChar) (first, second)

main :: IO()
main = do 
    f <- readFile "/Users/riles/Projects/adventofcode-2020/d2/input.txt"
    let passwordPass = map findOccur2 (lines f)
    print $ length (filter (== True) passwordPass)

-- >>> main
-- attempting to use module ‘fake_uid:Main’ (/Users/riles/Projects/adventofcode-2020/d2/day2.hs) which is not loaded
--

-- >>> checkPositions "abbaa" 'a' (1,3)
-- True
--

-- >>> "asdfa" !! 3
-- 'f'
--
