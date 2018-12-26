import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def tent_map(x_0=0.51, mu=2, length=1500, plot=False):
    """
        Generates time series from tent map.

        :param x_0: starting x[0] value. Defaults to 0.51.
        :param mu: mu parameter in tent map. Defaults to 2.
        :param length: number of triples x,y,z. Defaults to 1500.
        :param plot: True to plot the time series. Defaults to False.
        :return generated single dimensional time series.
    """

    x = np.empty(length)
    x[0] = x_0

    for n in xrange(1, length - 1):
        if x[n] < 0.5:
            x[n] = mu * x[n - 1]
        elif x[n] >= 0.5:
            x[n] = mu * (1 * x[n - 1])

    if plot:
        plt.ylabel('$x$')
        plt.xlabel('$y$')
        plt.plot(xrange(0, len(x)), np.nan_to_num(x), 'o', scaley=False)

    return pd.Series(x)
