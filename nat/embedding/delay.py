import os

import matplotlib.pyplot as plt
import pandas as pd
from tisean import delay as tisean_delay


def delay_vector(x, m=1, num_components=1, d=1, plot=False):
    """
        Uses tisean library to compute delay vectors from time series.

        More info:
        http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/docs/docs_c/delay.html
    :param m: embedded dim. Defaults to 1.
    :param x: time series.
    :param d: delay to use. Defaults to 1.
    :param num_components: number of components in time series (for multivariate data, it is more than 1).
                            Defaults to 1.
    :param plot: True to plot the time series. Defaults to False.
    :return: delay vectors
    """

    data, stderr = tisean_delay(data=x, m=m, M='{0}'.format(num_components), d=d)

    res = pd.read_csv(data, sep=' ', header=None)
    # Weird spaces in tisean delay output, so this removes last column to solve this
    res.drop(res.columns[[len(res.columns) - 1]], axis=1, inplace=True)
    col_size = len(res.columns)

    if plot:
        if col_size == 1:
            y = res.ix[:, 0].values
            plt.xlabel('$x(t)$')
            plt.ylabel('$x(t+{0})$'.format(d))
            plt.plot(x[0:len(y)], y, 'o')
        elif col_size == 2:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.set_xlabel('$x(t)$')
            ax.set_ylabel('$x(t+{0})$'.format(d - 1))
            ax.set_zlabel('$x(t+{0})$'.format(d))

            z = res.ix[:, 0].values
            y = res.ix[:, 1].values
            ax.plot(x[0:len(y)], y, z, 'o')

    return res
