from ..embedding import default_delay
import math
from tisean import d2
import tempfile
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ..utilities import get_subsets_by_count, get_percentage_diff, find_slope


def corr_dim_fast(x, min_m=1, max_m=10, d=None, t=0, c=1, epsilon=0.05, num_epsilons=100, r_min=None, r_max=None,
                  plot=False):
    """
        Uses tisean library to compute Correlation dimension (D_2).
        Also returns embedded dimension.

        More info:
        http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/docs/docs_c/d2.html

    :param x: time series.
    :param min_m: minimal embedding dimension.
    :param max_m: maximal embedding dimension.
    :param d: delay to use, if None calculates delay using :func default_delay.
    :param t: theiler window
    :param plot: True to plot the time series. Defaults to False.
    :return: approximated correlation dimension value, ceil of approximated correlation dimension value
    """
    if max_m is None or math.isnan(max_m):
        max_m = min_m
    assert min_m <= max_m

    if d is None:
        d = default_delay(x=x, plot=plot)

    tmp_name = next(tempfile._get_candidate_names())
    tmp_file = tmp_name + '.c2'
    d2(data=x, M='{0},{1}'.format(min_m, max_m), d=d, t=t,
       o=tmp_name, c=c, r=r_min, R=r_max, hashtag=num_epsilons)
    if os.path.getsize(tmp_file) == 0:
        return float('NaN'), None

    # first column: epsilon (in units chosen)
    # second column: correlation sum
    res = pd.read_csv(tmp_file, header=None, delimiter=' ', skip_blank_lines=True,
                      comment='#', names=['x', 'y'])
    if res.empty:
        return float('nan'), None

    os.remove(tmp_name + '.c2')
    os.remove(tmp_name + '.d2')
    os.remove(tmp_name + '.stat')
    os.remove(tmp_name + '.h2')

    subsets = get_subsets_by_count(num_epsilons, len(res['x']))
    dims = np.empty(len(subsets))
    i = 0
    if plot:
        fig = plt.figure()
        plt.ylabel('$\log_{10} C_{(m)}(r)$')
        plt.xlabel("$\log_{10} r$")

    for first, last in subsets:
        x = np.log10(res[first:last]['x'].values)
        y = np.log10(res[first:last]['y'].values)

        dims[i] = find_slope(x, y, epsilon=y.std() / 2, plot=plot)

        # if m is not None and i == m - 1:
        #     return dims[i], m
        i += 1

    if plot:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlabel("$m$")
        ax.set_ylabel('$\\bar{D_2}^{(m)}$')
        plt.plot(xrange(1, len(dims) + 1), dims)

    for embedded_dim in xrange(0, len(dims) - 1):

        if embedded_dim == 0:
            prev = dims[embedded_dim]
        else:
            prev = dims[embedded_dim - 1]

        curr_dim = dims[embedded_dim]
        next_dim = dims[embedded_dim + 1]
        ceil_dim = math.ceil(curr_dim)
        # print get_percentage_diff(curr, prev), get_percentage_diff(curr, next), curr
        if get_percentage_diff(curr_dim, prev) <= epsilon and get_percentage_diff(curr_dim, next_dim) <= epsilon:
            return curr_dim, ceil_dim

    return None, None
