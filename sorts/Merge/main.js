/**
 * Merge sort algorithm.
 * @param {Array} xs -- list of elements
 * @param {Function} comare -- function that defines the sort order
 *
 * @returns {Array} -- the sorted list
 */
var mergeSort = function(xs, compare) {
    var xsSorted = xs.slice();

    var helper = function(p, r) {
        if (p === r - 1) {
            return;
        }

        var q = Math.round((p + r) / 2);

        helper(p, q);
        helper(q, r);
        merge(p, q, r);
    };

    var merge = function(p, q, r) {
        if (p === q || q === r) {
            return;
        }

        var ls = xsSorted.slice(p, q);
        var rs = xsSorted.slice(q, r);

        var i = 0;
        var j = 0;
        var k;

        for (k = p; k < r; k++) {
            if (compare(rs[j], ls[i])) {
                xsSorted[k] = rs[j++];

                if (j === r - q) {
                    xsSorted.splice.apply(xsSorted, [k + 1, r - k - 1].concat(ls.slice(i)));
                    break;
                }
            } else {
                xsSorted[k] = ls[i++];

                if (i === q - p) {
                    xsSorted.splice.apply(xsSorted, [k + 1, r - k - 1].concat(rs.slice(j)));
                    break;
                }
            }
        }
    };

    helper(0, xs.length);

    return xsSorted;
}

exports.main = mergeSort;
