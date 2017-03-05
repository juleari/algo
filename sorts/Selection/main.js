/**
 * Selection sort algorithm.
 * @param {Array} xs -- list of elements
 * @param {Function} comare -- function that defines the sort order
 *
 * @returns {Array} -- the sorted list
 */
var selectionSort = function(xs, compare) {
    var xsSorted = xs.slice();
    var n = xsSorted.length;
    var min, minIndex, i;

    for (var j = 0; j < n - 1; j++) {
        min = xsSorted[j];
        minIndex = j;

        for (i = j + 1; i < n; i++) {
            if (compare(xsSorted[i], min)) {
                min = xsSorted[i];
                minIndex = i;
            }
        }

        xsSorted.splice(minIndex, 1)
        xsSorted.splice(j, 0, min)
    }

    return xsSorted;
}

exports.main = selectionSort;
