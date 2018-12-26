from ..tisean import low121
import pandas as pd
import matplotlib.pyplot as plt


def low_pass_filter(x, num_iter=1, plot=False):
    """
        Uses tisean library to compute simple Low pass filter in the time domain.


        More info:
        http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/docs/docs_c/low121.html

        :param x: input time series.
        :param num_iter: number of iterations. Defaults to 1.
        :param plot: True to plot the time series. Defaults to False.
        :return filtered time series.
    """
    #

    data = low121(data=x, i=num_iter)

    res = pd.read_csv(data, sep='\s+', header=None, names=['x'])
    if plot:
        plt.plot(xrange(0, len(res)), res['x'])
    return res['x']
