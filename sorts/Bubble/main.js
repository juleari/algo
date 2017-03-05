var swap = function(xs, i, j) {
    var t = xs[i];
    xs[i] = xs[j];
    xs[j] = t;
}

/**
 * Bubble sort algorithm.
 * @param {Array} xs -- list of elements
 * @param {Function} comare -- function that defines the sort order
 *
 * @returns {Array} -- the sorted list
 */
var bubbleSort = function(xs, compare) {
    var xsSorted = xs.slice();
    var n = xs.length;

    for (var i = 0; i < n - 1; i++) {
        for (var j = n - 1; j > i; j--) {
            if (compare(xsSorted[j], xsSorted[j - 1])) {
                swap(xsSorted, j, j - 1);
            }
        }
    }

    return xsSorted;
}

exports.main = bubbleSort;
