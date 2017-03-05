'''
Bubble sort algorithm.
@param xs -- list of elements
@param comare -- function that defines the sort order

@returns -- the sorted list
'''
def bubble_sort(xs, compare):
    sorted_xs = xs[:]
    n = len(xs)

    for i in range (n - 1):
        for j in range(n - 1, i, -1):
            if compare(sorted_xs[j], sorted_xs[j - 1]):
                sorted_xs[j], sorted_xs[j - 1] = sorted_xs[j - 1], sorted_xs[j]

    return sorted_xs

main = bubble_sort

if __name__ == '__main__':
    print main([1, 9, 2, 3, 4, 10, 10, 12, 5, 7], lambda x, y: x > y)
