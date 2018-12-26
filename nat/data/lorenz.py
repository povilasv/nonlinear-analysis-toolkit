import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ..tisean import lorenz


def lorenz_equations(f=100, r=28, sigma=10, b=8.0 / 3, x=10000, length=1500, plot=False):
    """
        Uses tisean library to compute time series from lorenz equations.

        More info:
        http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/docs/docs_f/lorenz.html

        :param f: sample points per unit time. Defaults to 100.
        :param r: parameter r. Defaults to 28.
        :param sigma: parameter sigma. Defaults to 10.
        :param b: parameter b. Defaults to 8/3
        :param x: number of transients discarded. Defaults to 10000.
        :param length: number of triples x,y,z. Defaults to 1500.
        :param plot: True to plot the time series. Defaults to False.
        :return generated three dimensional time series.
      """

    data, stderr = lorenz(l=length - 1, f=f, R=r, S=sigma, B=b, x=x)

    res = pd.read_csv(data, sep='\s+', header=None, names=['x', 'y', 'z'])
    if plot:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.set_zlabel('$z$')

        ax.plot(res['x'], res['y'], res['z'], 'o')

    return res['x'], res['y'], res['z']
