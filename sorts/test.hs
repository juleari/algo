-- ghci Test.hs
-- print (runTests Data.data_in_xs Data.data_in_cmp Data.data_out [])

import Insertion.Insertion as Insertion
import Data

getErrorString :: [Integer] -> [Integer] -> [Integer] -> String
getErrorString x_in x_out x_res = "Error:\n  data in:  " ++ (show x_in) ++ "\n  expected: " ++ (show x_out) ++ "\n  recieved: " ++ (show x_res)

singleTest :: [Integer] -> (Integer -> Integer -> Bool) -> [Integer] -> String
singleTest x_in x_cmp x_out | (Insertion.insertion_sort x_in x_cmp) == x_out = ""
                            | otherwise = getErrorString x_in x_out (Insertion.insertion_sort x_in x_cmp)

reduce :: (a -> a -> a) -> a -> [a] -> a
reduce op acc [] = acc
reduce op acc (x : xs) = reduce op (op acc x) xs

getTestsInfo :: [String] -> String
getTestsInfo [] = "tests OK"
getTestsInfo res = reduce (++) "" (map (++ "\n") res)

filledStr :: String -> Bool
filledStr "" = False
filledStr s  = True

runTests :: [[Integer]] -> [(Integer -> Integer -> Bool)] -> [[Integer]] -> [String] -> String
runTests [] [] [] res = "run " ++ show (length res) ++ " tests:\n" ++ getTestsInfo (filter filledStr res)
runTests (x_in : xs_in) (x_cmp : xs_cmp) (x_out : xs_out) res =
    runTests xs_in xs_cmp xs_out (res ++ [singleTest x_in x_cmp x_out])
