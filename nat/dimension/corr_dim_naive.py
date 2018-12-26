from ..embedding import default_delay
import math
import os
from ..tisean import c2naive
import pandas as pd
import numpy as np
from ..utilities import get_subsets_by_count, find_slope
import matplotlib.pyplot as plt
import tempfile


# TODO: params
def corr_dim_naive(x, min_m=1, max_m=10, d=None, t=0, plot=False):
    """
        Uses tisean library to compute Correlation dimension.

        More info:
        http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/docs/docs_f/c2naive.html

    :param x: time series.
    :param min_m: minimal embedding dimension.
    :param max_m: maximal embedding dimension.
    :param d: delay to use, if None calculates delay using :func default_delay.
    :param t: theiler window
    :param s: number of iterations.
    :param plot: True to plot the time series. Defaults to False.
    :return: approximated correlation dimension value, ceil of approximated correlation dimension value
    """
    if max_m is None or math.isnan(max_m):
        max_m = min_m
    assert min_m <= max_m

    # Column to be read
    c = 1

    if d is None:
        d = default_delay(x=x, plot=plot)

    tmp_name = next(tempfile._get_candidate_names())
    c2naive(data=x, M=max_m, m=min_m, d=d, t=t, c=c, o=tmp_name)

    if os.path.getsize(tmp_name) == 0:
        return None, None

    # first column: epsilon (in units chosen)
    # second column: correlation sum
    res = pd.read_csv(tmp_name, header=None, delim_whitespace=True, skip_blank_lines=True,
                      comment='#',
                      names=['x', 'y']);
    os.remove(tmp_name)

    if res.empty:
        return None, None

    res_len = len(res['x'])

    subsets = get_subsets_by_count(int(res_len / max_m), res_len)
    dims = np.empty(len(subsets))
    i = 0
    if plot:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlabel("$\epsilon$")
        ax.set_ylabel('$C(m,\epsilon)$')

    for first, last in subsets:
        x = res[first:last]['x'].values
        y = res[first:last]['y'].values

        dims[i] = find_slope(x, y, epsilon=y.std() / 2, plot=plot)
        i += 1

    for embedded_dim in xrange(1, len(dims)):
        corr_dim = dims[embedded_dim]
        ceil_dim = math.ceil(corr_dim)
        if embedded_dim > ceil_dim:
            return dims[ceil_dim], ceil_dim

    return corr_dim, embedded_dim
