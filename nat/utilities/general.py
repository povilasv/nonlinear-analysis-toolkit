import matplotlib.pyplot as plt
import numpy as np
import math
from ..rdp import find_longest_line


def get_subsets(x):
    index = 0
    previous = x[index]
    start = index
    res = []
    for val in x:
        if val >= previous:
            previous = val
        else:
            res.append((start, index))
            start = index
            previous = val
        index = index + 1
    res.append((start, index))
    return res


def get_subsets_by_count(count, length):
    total_counts = int(math.ceil(float(length) / count))
    res = []
    for i in xrange(0, total_counts, 1):
        start = i * count
        end = (i + 1) * count
        if end > length:
            end = length

        res.append((start, end))
    return res


def get_percentage_diff(orig, new):
    return (float(orig) - float(new)) / float(orig)


def drop_ninf_pinf(x, y):
    if x.shape == (0L,):
        return x
    x[x == (np.NINF or np.PINF)] = None
    indices = ~np.isnan(x)
    x = x[indices]
    y = y[indices]
    return x, y


def find_slope(x, y, epsilon=0.25, plot=False):
    """
        Uses RDP algorithm to find line segments.
        Then chooses line with largest delta y.

    :param x:
    :param y:
    :param epsilon:
    :param plot: when True, plots figures.
    :return:
    """

    assert len(x) == len(y)

    if len(x) == 1:
        return None
    y, x = drop_ninf_pinf(y, x)

    x_start, x_end = find_longest_line(x, y, epsilon=epsilon)
    x_part = x[x_start:x_end + 1]
    y_part = y[x_start:x_end + 1]
    if y_part.shape == (0L,):
        return None

    m, b = np.polyfit(x_part, y_part, deg=1)
    if plot:
        plt.plot(x, y, '-')
        # ax.plot(x_part, m * x_part + b + line_above, 'r--')
    return m


def find_first_local_maxima(ys):
    start_idx = 1
    ys = ys[start_idx:]
    max = float('-inf')
    i = start_idx
    for y in ys:
        if y >= max:
            max = y
        else:
            return i, max
        i += 1

    return None, None
