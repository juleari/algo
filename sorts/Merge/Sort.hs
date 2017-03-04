module Merge.Sort where
-- Merge sort algorithm.
merge_sort :: [a] -> (a -> a -> Bool) -> [a]
merge_sort xs cmp = helper cmp xs

helper :: (a -> a -> Bool) -> [a] -> [a]
helper cmp []  = []
helper cmp [x] = [x]
helper cmp xs  = merge cmp (helper cmp (gfst xs)) (helper cmp (glst xs))

merge :: (a -> a -> Bool) -> [a] -> [a] -> [a]
merge cmp [] ys = ys
merge cmp xs [] = xs
merge cmp (x : xs) (y : ys) | cmp y x   = y : merge cmp (x : xs) ys
                            | otherwise = x : merge cmp xs (y : ys)

substr from len = take len . drop from
gfst xs = substr 0 (ceiling (fromIntegral (length xs) / 2)) xs
glst xs = substr (ceiling (fromIntegral (length xs) / 2)) (length xs) xs

sort = merge_sort
