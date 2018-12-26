import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from ..tisean import ikeda


def ikeda_map(re=0.41, im=0.41, a=0.4, b=6.0, c=0.9, length=1500, plot=False):
    """
        Uses tisean library to compute time series from ikeda map.

        More info:
        http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/docs/docs_f/ikeda.html

        :param re: initial Re(z). Defaults to 0.41.
        :param im: initial Im(z) Defaults to 0.41.
        :param a: parameter a. Defaults to 0.4.
        :param b: parameter b. Defaults to 6.0.
        :param c: parameter c Defaults to 0.9.
        :param length: length of generated time series. Defaults to 1500.
        :param plot: True to plot the time series. Defaults to False.
        :return generated two dimensional time series.
    """

    data, stderr = ikeda(l=length, R=re, I=im, A=a, B=b, C=c)

    res = pd.read_csv(data, sep='\s+', header=None, names=['x', 'y'])

    if plot:
        plt.ylabel('$x$')
        plt.xlabel('$y$')
        plt.plot(res['x'], res['y'], 'o')

    return res['x'], res['y']
