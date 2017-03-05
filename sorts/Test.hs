-- ghc -o Test Test.hs
-- ./Test

-- ghci Test.hs

import Bubble.Sort as Sort
import Data.Data as Data
import Text.Printf
import System.CPUTime

getErrorString :: [Integer] -> [Integer] -> [Integer] -> String
getErrorString x_in x_out x_res = "Error:\n  data in:  " ++ (show x_in) ++ "\n  expected: " ++ (show x_out) ++ "\n  recieved: " ++ (show x_res)

singleTest :: [Integer] -> (Integer -> Integer -> Bool) -> [Integer] -> String
singleTest x_in x_cmp x_out | (Sort.sort x_in x_cmp) == x_out = ""
                            | otherwise = getErrorString x_in x_out (Sort.sort x_in x_cmp)

reduce :: (a -> a -> a) -> a -> [a] -> a
reduce op acc [] = acc
reduce op acc (x : xs) = reduce op (op acc x) xs

getTestsInfo :: [String] -> String
getTestsInfo [] = "tests OK\n"
getTestsInfo res = reduce (++) "" (map (++ "\n") res)

filledStr :: String -> Bool
filledStr "" = False
filledStr s  = True

runTests :: [[Integer]] -> [(Integer -> Integer -> Bool)] -> [[Integer]] -> [String] -> String
runTests [] [] [] res = "run " ++ show (length res) ++ " tests:\n" ++ getTestsInfo (filter filledStr res)
runTests (x_in : xs_in) (x_cmp : xs_cmp) (x_out : xs_out) res =
    runTests xs_in xs_cmp xs_out (res ++ [singleTest x_in x_cmp x_out])

main :: IO ()
main = do
    start <- getCPUTime
    let res = runTests Data.data_in_xs Data.data_in_cmp Data.data_out []
    end <- getCPUTime
    let diff = (fromIntegral (end - start)) / (10^12)
    printf "runTests: %0.7f sec\n" (diff :: Double)
    putStr res
