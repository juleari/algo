# import errors
# import compare

'''
Selection sort algorithm.
@param xs -- list of elements
@param comare -- function that defines the sort order

@returns -- the sorted list
'''
def selection_sort(xs, compare):
    sorted_xs = xs[:]
    n = len(sorted_xs)

    for j in range(0, n - 1):
        min_v, min_i = sorted_xs[j], j

        for i in range(j + 1, n):
            if compare(sorted_xs[i], min_v):
                min_v, min_i = sorted_xs[i], i

        sorted_xs = sorted_xs[:j] +\
                    [min_v] +\
                    sorted_xs[j : min_i] +\
                    sorted_xs[min_i + 1:]

    return sorted_xs

main = selection_sort

if __name__ == '__main__':
    print main([1, 9, 2, 3, 4, 10, 10, 12, 5, 7], lambda x, y: x > y)
