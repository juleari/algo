module Merge.Sort where
-- Merge sort algorithm.
merge_sort :: [a] -> (a -> a -> Bool) -> [a]
merge_sort xs cmp = helper cmp xs

helper :: (a -> a -> Bool) -> [a] -> [a]
helper cmp []  = []
helper cmp [x] = [x]
helper cmp xs  = merge cmp (helper cmp (left xs)) (helper cmp (right xs))

merge :: (a -> a -> Bool) -> [a] -> [a] -> [a]
merge cmp [] rs = rs
merge cmp ls [] = ls
merge cmp (l : ls) (r : rs) | cmp r l   = r : merge cmp (l : ls) rs
                            | otherwise = l : merge cmp ls (r : rs)

half_length xs = ceiling (fromIntegral (length xs) / 2)
left  xs = take (half_length xs) xs
right xs = take (half_length xs) (drop (half_length xs) xs)

sort = merge_sort
