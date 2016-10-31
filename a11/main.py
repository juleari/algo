def listLoop(xs):
    n = len(xs)

    statuses = [False] * n

    if n == 0:
        return 'ok'

    i = 0
    k = 0

    while True:
        if i >= n:
            return 'right in %i' % k

        if i < 0:
            return 'left in %i' % k

        if statuses[i]:
            return 'error loop %i' % xs[i]

        statuses[i] = True
        i += xs[i]
        k += 1

def main(xs):
    return listLoop(xs)

if __name__ == '__main__':
    print main([1, 2, 0, -1, 4, -2, 0, 3])
