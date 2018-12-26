import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def logistic_map(x_0=0.51, r=4, length=1500, plot=False):
    """
        Generates time series from logistic map.
        :param x_0: starting x[0] value. Defaults to 0.51.
        :param r: r parameter in logistic map. Defaults to 4.
        :param length: length of generated time series. Defaults to 1500.
        :param plot: True to plot the time series. Defaults to False.
        :return generated single dimensional time series.
    """

    x = np.empty(length)
    x[0] = x_0

    for n in xrange(1, length - 1):
        x[n] = x[n - 1] * r * (1 - x[n - 1])

    if plot:
        plt.ylabel('$x(t)$')
        plt.xlabel('$t$')
        plt.plot(xrange(0, len(x)), x, 'o')

    return pd.Series(x)
