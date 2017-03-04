'''
Merge sort algorithm.
@param xs -- list of elements
@param comare -- function that defines the sort order

@returns -- the sorted list
'''
def merge_sort(xs, compare):
    sorted_xs = xs[:]

    def helper(p, r):
        if p < r - 1:
            q = int(round((p + r) / 2.0))
            helper(p, q)
            helper(q, r)
            merge(p, q, r)

    def merge(p, q, r):
        if p == q or q == r:
            return

        ls = sorted_xs[p : q]
        rs = sorted_xs[q : r]

        i = j = 0

        for k in range(p, r):
            # compare in reverse,
            # to save the order of equal elements
            if compare(rs[j], ls[i]):
                sorted_xs[k] = rs[j]
                j += 1

                if j == r - q:
                    sorted_xs[k + 1 : r] = ls[i:]
                    break
            else:
                sorted_xs[k] = ls[i]
                i += 1

                if i == q - p:
                    sorted_xs[k + 1 : r] = rs[j:]
                    break

    helper(0, len(xs))

    return sorted_xs

main = merge_sort

if __name__ == '__main__':
    print main([1, 9, 2, 3, 4, 10, 10, 12, 5, 7], lambda x, y: x > y)
