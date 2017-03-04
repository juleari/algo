'''
Merge sort algorithm.
@param xs -- list of elements
@param comare -- function that defines the sort order

@returns -- the sorted list
'''
def merge_sort(xs, compare):
    sorted_xs = xs[:]

    def merge_sort_helper(p, r):
        if p < r - 1:
            q = int(round((p + r) / 2.0))
            merge_sort_helper(p, q)
            merge_sort_helper(q, r)
            merge(p, q, r)

    def merge(p, q, r):
        L = sorted_xs[p : q]
        R = sorted_xs[q : r]

        if p == q or q == r:
            return

        i = j = 0

        for k in range(p, r):
            # compare in reverse,
            # to save the order of equal elements
            if compare(R[j], L[i]):
                sorted_xs[k] = R[j]
                j += 1

                if j == r - q:
                    sorted_xs[k + 1 : r] = L[i:]
                    break
            else:
                sorted_xs[k] = L[i]
                i += 1

                if i == q - p:
                    sorted_xs[k + 1 : r] = R[j:]
                    break

    merge_sort_helper(0, len(xs))

    return sorted_xs

main = merge_sort

if __name__ == '__main__':
    print main([1, 9, 2, 3, 4, 10, 10, 12, 5, 7], lambda x, y: x > y)
