from math import floor, ceil, pow, sqrt, log
from decimal import getcontext, Decimal

def lg_n(time):
    getcontext().prec = 1
    getcontext().Emax = 999999999999
    return Decimal(2) ** Decimal(time)

def sqrt_n(time):
    return time * time

def fn_n(time):
    return time

def fn_n_lg_n(n):
    return n * log(n, 2)

def bin_n_lg_n(begin, end, target):
    if begin == end or begin == end - 1:
        return begin

    mid_n = begin + floor((end - begin) / 2)
    mid_value = fn_n_lg_n(mid_n)

    if mid_value < target:
        return bin_n_lg_n(mid_n, end, target)
    elif mid_value == target:
        return mid_n
    else:
        return bin_n_lg_n(begin, mid_n, target)

def n_lg_n(time):
    return bin_n_lg_n(1, floor(time / 2), time)

def n_2(time):
    return floor(sqrt(time))

def n_3(time):
    exact = pow(time, 1.0/3)
    return ceil(exact) if ceil(exact) ** 3 == time else floor(exact)

def exp_n(time):
    return floor(log(time, 2))

def factorial(time):
    n = 3
    value = 6
    while value <= time:
        n += 1
        value *= n
    return n - 1
