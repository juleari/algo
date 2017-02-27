var data = require('./data');

var getErrorString = (input, output, result) =>
    `Error:\n input: ${input}\n expected: ${output}\n recieved: ${result}`;

var getErrorsInfo = results =>
    [`${results.length} failed`].concat(results).join('\n');

var getTestsInfo = (testsLen, results) =>
    `run ${testsLen} tests:\n${ results.length ? getErrorsInfo(results) : 'tests OK' }`;

var singleTest = function(func, input, output) {
    var result = func.apply(this, input);
    return output.toString() !== result.toString() && getErrorString(input, output, result);
}

var runTests = function(func, data) {
    var testsLen = data.length;
    var results = data
        .map(dataElem => singleTest(func, dataElem.input, dataElem.output))
        .filter(Boolean);

    return getTestsInfo(testsLen, results);
}

var name = process.argv[2];

var sort = require(`./${name}/main`);

console.time('runTests');
var info = runTests(sort.main, data.data);
console.timeEnd('runTests');

console.log( info );
