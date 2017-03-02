module Insertion.Insertion where
-- Insertion sort algorithm.
insertion_sort :: [a] -> (a -> a -> Bool) -> [a]
insertion_sort xs cmp = helper [] xs cmp

helper :: [a] -> [a] -> (a -> a -> Bool) -> [a]
helper xs [] cmp = xs
helper xs (y : ys) cmp = helper (insert [] xs y cmp) ys cmp

insert :: [a] -> [a] -> a -> (a -> a -> Bool) -> [a]
insert xs [] x cmp = [x] ++ xs
insert xs ys x cmp | cmp y x   = insert ([y] ++ xs) (heads ys) x cmp
                   | otherwise = ys ++ [x] ++ xs
                   where y = last ys

heads :: [a] -> [a]
heads (x : []) = []
heads (x : xs) = x : heads xs
