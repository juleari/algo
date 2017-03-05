module Bubble.Sort where
-- Bubble sort algorithm.
bubble_sort :: (a -> a -> Bool) -> [a] -> [a]
bubble_sort cmp xs = helper cmp [] [] xs

helper :: (a -> a -> Bool) -> [a] -> [a] -> [a] -> [a]
helper cmp ss [] []  = ss
helper cmp ss [] [x] = x : ss
helper cmp ss bs [x] = helper cmp (x : ss) [] bs
helper cmp ss bs (x : y : xs) | cmp y x   = helper cmp ss (bs ++ [y]) (x : xs)
                              | otherwise = helper cmp ss (bs ++ [x]) (y : xs)

sort xs cmp = bubble_sort cmp xs
