module Selection.Sort where
-- Selection sort algorithm.
selection_sort :: (a -> a -> Bool) -> [a] -> [a]
selection_sort cmp []  = []
selection_sort cmp [x] = [x]
selection_sort cmp (x : xs) = helper cmp x 1 [x] xs

helper :: (a -> a -> Bool) -> a -> Int -> [a] -> [a] -> [a]
helper cmp m i [] [] = [m]
helper cmp m i [] [y]  | cmp y m   = y : [m]
                       | otherwise = m : [y]
helper cmp m i xs [y]  | cmp y m   = y : [m] ++ helper cmp z 0 [z] zs
                       | otherwise = m : [y] ++ helper cmp z 0 [z] zs
                        where zzs = take i xs ++ drop (i + 1) xs
                              z = head zzs
                              zs = tail zzs
helper cmp m i xs (y : ys)  | cmp y m   = helper cmp y l (xs ++ [y]) ys
                            | otherwise = helper cmp m i (xs ++ [y]) ys
                            where l = fromIntegral (length xs)

sort xs cmp = selection_sort cmp xs

-- < [1 3 2]
-- helper < 1 0 [1] [3 2]
-- helper < 1 0 [1 3] [2]
-- [1 2] helper < z 0 [] zs
--                zzs = [3]
--                z = 3
--                zs = []
-- helper < 3 0 [] []
