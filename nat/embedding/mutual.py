import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ..tisean import mutual as tisean_mutual
from ..embedding import DELAY_SEARCH_LIMIT, DELAY_SEARCH_START


# TODO: params
# TODO: cleanup
def mutual_information(x, max_d=1000, boxes=16, plot=False):
    """
        Uses tisean library to get time delay using mutual information of the data for signal x.
        More info:
        http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.0/docs/docs_c/mutual.html

    :param boxes: number of boxes to partition. Defaults to 16.
    :param x: signal.
    :param max_d: maximal time delay. Defaults to 1000.
    :param plot: True to plot the time series. Defaults to False.
    :return: estimated time delay, or None if not found.
    """

    data, stderr = tisean_mutual(data=x, D=max_d, b=boxes)
    # First column: delay
    # Second column: mutual information.
    res = pd.read_csv(data, header=None, delimiter=' ', names=["delay", "mutual"], comment='#',
                      dtype={"delay": np.int32, "mutual": np.float32})
    print stderr.getvalue()
    x = res['delay']
    y = res['mutual']

    if plot:
        # plt.figure()
        # plt.ylabel('$I(x(t),x(t+\Delta T))$')
        plt.ylabel('Mutual information')
        plt.xlabel('$\Delta T$')
        plt.plot(x, y, '-')

    return x, y


# TODO: params
def find_mutual_min(x, max_d=1000, plot=False):
    x, y = mutual_information(x=x, max_d=max_d, plot=plot)
    i = 0
    # First local minimum of mutual information
    # TODO: move to utils

    curr_y = float('inf')
    for y_val in y:
        if y_val < curr_y:
            curr_y = y_val
        else:
            return x[i]
        i += 1

    return None


def delay_mutual(x, plot=False):
    """

    :param x: signal.
    :param plot: True to plot the time series. Defaults to False.
    :return: estimated delay.
    """
    max_d = DELAY_SEARCH_START
    limit = DELAY_SEARCH_LIMIT
    d = None
    while d is None:
        d = find_mutual_min(x, max_d=max_d, plot=plot)
        max_d *= 10
        if max_d >= limit:
            return None
    return d
