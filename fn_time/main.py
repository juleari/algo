from tabulate import tabulate
from fns import lg_n, sqrt_n, fn_n, n_lg_n, n_2, n_3, exp_n, factorial

def count_fn_time(fn, time):
    return apply(fn, [time])

def table(times, functions):
    body = [
        [fn[1]] +
        [count_fn_time(fn[0], time[0]) for time in times] for fn in functions
    ]
    return tabulate(
        body,
        headers = [""] + [time[1] for time in times],
        numalign="right"
    )

if __name__ == '__main__':
    times = [
        (1000, "second"),
        (60 * 1000, "minute"),
        (60 * 60 * 1000, "hour"),
        (24 * 60 * 60 * 1000, "day"),
        (30 * 24 * 60 * 60 * 1000, "month"),
        (355 * 24 * 60 * 60 * 1000, "year"),
        ((355 * 3 + 356) * 25 * 24 * 60 * 60 * 1000, "century")
    ]
    functions = [
        (lg_n, "lg n"),
        (sqrt_n, "sqrt n"),
        (fn_n, "n"),
        (n_lg_n, "n lg n"),
        (n_2, "n^2"),
        (n_3, "n^3"),
        (exp_n, "2^n"),
        (factorial, "n!")
    ]

    print table(times, functions)
