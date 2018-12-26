from ..tisean import makenoise
import pandas as pd
import matplotlib.pyplot as plt


def add_noise(x, percentage=5, type='uniform', plot=False):
    """
        Uses tisean library to add noise to time series data.

        More info:
        http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/docs/docs_c/makenoise.html

        :param x:
        :param percentage:
        :param type: gaussian or uniform. Defaults to uniform.
        :param plot:
        :return: noisy time series.
      """
    if percentage == 0:
        return x

    if type == 'gaussian':
        data, stderr = makenoise(data=x, percentage=percentage, additional_params=['-g'])
    elif type == 'uniform':
        data, stderr = makenoise(data=x, percentage=percentage)

    res = pd.read_csv(data, sep='\s+', header=None, names=['x'])
    if plot:
        plt.ylabel('$x$')
        plt.xlabel('$y$')
        plt.plot(xrange(0, len(x)), res['x'], 'o')

    return res['x']
