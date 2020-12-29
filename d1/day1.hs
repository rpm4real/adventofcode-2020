--import System.IO(readFile, openFile)
--import System.Directory(getDirectoryContents)

makeInteger :: [String] -> [Int]
makeInteger = map read 

sumOptions :: [Int] -> [(Int, Int, Int, Int)]
sumOptions xs = [(x,y,x+y,x*y) | x <- xs, y <- xs, x+y == 2020]

sumOptions2 :: [Int] -> [(Int, Int, Int, Int, Int)]
sumOptions2 xs = [(x, y, z, x+y+z, x*y*z) | x <- xs, y <- xs, z <- xs, x+y+z == 2020]

main2 :: IO()
main2 = do 
    f <- readFile "/Users/riles/Projects/adventofcode-2020/d1/input.txt"
    let myInts = makeInteger $ lines f 
    print $ sumOptions myInts

-- >>> main2
-- [(1768,252,2020,445536),(252,1768,2020,445536)]
--

