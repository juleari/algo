def FindMaxAndMin2n(xs):
    n = len(xs)

    if n == 0:
        return None, None, True

    x = xs[0]
    if n == 1:
        return x, x, True

    y = xs[1]
    if x > y:
        max_ = x
        min_ = y
    else:
        min_ = x
        max_ = y

    c = 1

    for i in range(2, n - 1, 2):
        x = xs[i]
        y = xs[i + 1]

        if x > y:
            if x > max_:
                max_ = x
            if y < min_:
                min_ = y
        else:
            if x < min_:
                min_ = x
            if y > max_:
                max_ = y

        c += 3

    if n % 2 == 1:
        x = xs[n - 1]

        if x > max_:
            max_ = x
            c += 1
        elif x < min_:
            min_ = x

    return max_, min_, c < n * 2

def main(xs):
    return FindMaxAndMin2n(xs)

if __name__ == '__main__':
    print main([1, 2, 3, 4])
