from subprocess import call
import sys, os

TEST_PATH = 'runtest.py'

def getErrorString(input, output, result):
    return "Error:\n  data in:  %s\n  expected: %s\n  recieved: %s" %\
            (input, output, result)

def getErrorsInfo(results):
    return "\n".join(["%s failed" % len(results)] + results)

def getTestsInfo(len_tests, results):
    return "run %s tests:\n" % len_tests + \
        ("tests OK" if len(results) == 0 else getErrorsInfo(results))

def singleTest(func, input, output):
    result = apply(func, input)
    return output == result or getErrorString(input, output, result)

def runTests(func, inputs, outputs):
    len_tests = len(inputs)

    if len_tests != len(outputs):
        return "Can't run tests because the input data does not match the output"

    results = filter(lambda x: x != True,
                    [ singleTest(func, input, output)
                        for input, output in zip(inputs, outputs) ])

    return getTestsInfo(len_tests, results)

def generateTest(sort_name):
    return ('from test import runTests\n' +\
            'from %n.main import main\n' +\
            'from data import dataIn, dataOut\n\n' +\
            'print runTests(main, dataIn, dataOut)') % (sort_name)

def main():
    name = 'Insertion' if len(sys.argv) < 2 else sys.argv[1]
    testInner = generateTest(name)
    testFile = open(TEST_PATH, 'w')

    testFile.write(testInner)
    testFile.close()

    call('python %s' % TEST_PATH, shell=True)
    os.remove(TEST_PATH)

if __name__ == '__main__':
    main()
