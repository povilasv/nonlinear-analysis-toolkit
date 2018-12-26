import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def lozi_map(x_0=0.51, y_0=0.51, a=1.4, b=0.3, length=1500, plot=False):
    """
        Generates time series from lozi map.
        :param x_0: starting x[0] value. Defaults to 0.51.
        :param y_0: starting y[0] value. Defaults to 0.51.
        :param a: a parameter in lori map. Defaults to 1.4.
        :param b: b parameter in lori map. Defaults to 0.3.
        :param length: number of triples x,y,z. Defaults to 1500.
        :param plot: True to plot the time series. Defaults to False.
        :return generated two dimensional time series.
    """

    x = np.empty(length)
    y = np.empty(length)
    x[0] = x_0
    y[0] = y_0
    for n in xrange(1, length - 1):
        x[n + 1] = 1 - a * abs(x[n]) + y[n]
        y[n + 1] = b * x[n]

    if plot:
        plt.ylabel('$x$')
        plt.xlabel('$y$')
        plt.plot(x, y, 'o')

    return pd.Series(x), pd.Series(y)
