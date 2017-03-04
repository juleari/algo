module Merge.Sort where
-- Merge sort algorithm.
merge_sort :: (a -> a -> Bool) -> [a] -> [a]
merge_sort cmp []  = []
merge_sort cmp [x] = [x]
merge_sort cmp xs  = merge cmp (merge_sort cmp (left xs)) (merge_sort cmp (right xs))

merge :: (a -> a -> Bool) -> [a] -> [a] -> [a]
merge cmp [] rs = rs
merge cmp ls [] = ls
merge cmp (l : ls) (r : rs) | cmp r l   = r : merge cmp (l : ls) rs
                            | otherwise = l : merge cmp ls (r : rs)

half_length xs = ceiling (fromIntegral (length xs) / 2)
left  xs = take (half_length xs) xs
right xs = take (half_length xs) (drop (half_length xs) xs)

sort xs cmp = merge_sort cmp xs
