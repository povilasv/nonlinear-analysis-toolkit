from . import default_delay
from ..tisean import false_nearest as tisean_false_nearest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def embeded_dim_kennel(x, min_m=2, max_m=20, num_components=1, d=None, ratio_factor=10.0, t=0,
                       zero_tolerance=0.01, plot=False):
    """
        Uses tisean library to compute minimum embedded dimension using Kennel et al. 1992 algorithm.

        More info:
        http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.0/docs/docs_c/false_nearest.html
    :param x: time series.
    :param min_m: minimal embedding dimension to use.
    :param max_m: maximal embedding dimension to use.
    :param d: delay to use, if None calculates delay using :func find_autocorr_drop.
    :param zero_tolerance: tolerance factor for identifying min embedded dimension.
    :param t: theiler window
    :param ratio_factor: tolerance factor which determines when to specify nearest neighbour as false.
                            In Kennel et al. paper it is R_tol.
    :param num_components: number of components in time series (for multivariate data, it is more than 1).
    :param plot: True to plot the time series. Defaults to False.
    :return: minimal embedded dimension value.
    """
    assert min_m <= max_m

    if d is None:
        d = default_delay(x=x, plot=plot)

    data, stderr = tisean_false_nearest(data=x, m=min_m, M='{0},{1}'.format(num_components, max_m), t=t, f=ratio_factor,
                                        d=d)

    # first column: the dimension (counted like shown above)
    # second column: the fraction of false nearest neighbors
    # third column: the average size of the neighborhood
    # fourth column: the average of the squared size of the neighborhood
    res = pd.read_csv(data, sep=' ', names=['dimension', 'fraction', 'average', 'squared_average'],
                      dtype={"dimension": np.int32, "fraction": np.float32})
    #
    x = res.ix[:, 0].values
    y = res.ix[:, 1].values
    #
    if plot:
        plt.xlabel('d')
        plt.ylabel('fraction of false nearest neighbors')
        plt.plot(x, y)

    i = 0
    for y_val in y:
        if y_val < zero_tolerance:
            return x[i]
        i += 1

    return None
