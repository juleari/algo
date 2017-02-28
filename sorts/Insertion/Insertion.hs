module Insertion.Insertion where

heads :: [a] -> [a]
heads (x : []) = []
heads (x : xs) = x : heads xs

-- Insertion sort algorithm.
insertion_sort :: [a] -> (a -> a -> Bool) -> [a]
insertion_sort [] cmp = []
insertion_sort (x : xs) cmp = insertion_sort_helper x xs cmp

insertion_sort_helper :: a -> [a] -> (a -> a -> Bool) -> [a]
insertion_sort_helper x [] cmp = [x]
insertion_sort_helper x (xx : xxs) cmp = insertion_sort_ba xx [x] [] xxs cmp

insertion_sort_ba :: a -> [a] -> [a] -> [a] -> (a -> a -> Bool) -> [a]
insertion_sort_ba x [] xs [] cmp = x : xs
insertion_sort_ba x [] xs (a : as) cmp = insertion_sort_ba a (x : xs) [] as cmp
insertion_sort_ba x bs xs [] cmp | cmp (last bs) x = insertion_sort_ba x (heads bs) ((last bs) : xs) [] cmp
                                 | otherwise       = bs ++ (x : xs)
insertion_sort_ba x bs xs (a : as) cmp | cmp (last bs) x = insertion_sort_ba x (heads bs) ((last bs) : xs) (a : as) cmp
                                       | otherwise       = insertion_sort_ba a (bs ++ (x : xs)) [] as cmp
