# This code is based on
# https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm

from math import sqrt
import numpy as np

def perpendicular_distance(x, y, x_start, y_start, x_end, y_end):
    n = abs((x_end - x_start) * (y_start - y) - (x_start - x) * (y_end - y_start))
    d = sqrt((x_end - x_start) ** 2 + (y_end - y_start) ** 2)
    return n / d


def find_line(x, y, begin=0, end=None, epsilon=1):
    if end is None:
        end = len(x) - 1

    dmax = 0
    index = 0
    for i in range(begin + 1, end):
        d = perpendicular_distance(x[i], y[i], x[begin], y[begin], x[end], y[end])

        if d > dmax:
            index = i
            dmax = d

    if dmax >= epsilon:
        results = find_line(x, y, begin=begin, end=index, epsilon=epsilon) + find_line(x, y, begin=index, end=end,
                                                                                       epsilon=epsilon)
    else:
        results = [(x[begin], y[begin], x[end], y[end])]

    return results


def find_longest_line(x, y, begin=0, end=None, epsilon=1):
    ls_values = find_line(x=x, y=y, begin=begin, end=end, epsilon=epsilon)
    d = 0
    res_x_start = None
    res_x_end = None

    for val in ls_values:
        x_start = val[0]
        y_start = val[1]
        x_end = val[2]
        y_end = val[3]
        d_norm = (y_end - y_start) ** 2
        if d_norm >= d:
            d = d_norm
            res_x_start = x_start
            res_x_end = x_end

    return np.where(x == res_x_start)[0], np.where(x == res_x_end)[0]
