# import errors
# import compare

'''
Insertion sort algorithm.
@param xs -- list of elements
@param comare -- function that defines the sort order

@returns -- the sorted list
'''
def insertion_sort(xs, compare):
    sorted_xs = xs[:]

    for j in range(1, len(sorted_xs)):
        key = sorted_xs[j]

        i = j - 1
        while i > -1 and compare(key, sorted_xs[i]):
            sorted_xs[i + 1] = sorted_xs[i]
            i -= 1

        sorted_xs[i + 1] = key

    return sorted_xs

def main(xs, compare):
    return insertion_sort(xs, compare)

if __name__ == '__main__':
    print insertion_sort([1, 9, 2, 3, 4, 10, 10, 12, 5, 7], lambda x, y: x > y)
