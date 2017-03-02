/**
 * Inseption sort algorithm.
 * @param {Array} xs -- list of elements
 * @param {Function} comare -- function that defines the sort order
 *
 * @returns {Array} -- the sorted list
 */
var insertionSort = function(xs, compare) {
    var xsSorted = xs.slice();
    var key, i;

    for (var j = 1; j < xs.length; j++) {
        key = xsSorted[j];

        i = j - 1;
        while (i > -1 && compare(xsSorted[i], key)) {
            xsSorted[i + 1] = xsSorted[i];
            i -= 1;
        }

        xsSorted[i + 1] = key;
    }

    return xsSorted;
}

exports.main = insertionSort;
