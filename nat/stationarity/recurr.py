from ..tisean import recurr
from ..utilities import get_subsets
import matplotlib.pyplot as plt
import pandas as pd


def recurrence_plot(x, num_components=1, m=1, d=None, neighbourhood_size=None, plot=False):
    """
        Uses tisean library to compute recurrence plot


        More info:
        http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/docs/docs_c/recurr.html
        :param d: delay
        :param m: embedding dimension
        :param plot: True to plot the time series. Defaults to False.
    """
    #

    data, stderr = recurr(data=x, m='{0},{1}'.format(num_components, m), d=d, r=neighbourhood_size)

    res = pd.read_csv(data, sep='\s+', header=None, names=['x', 'y'])
    if plot:
        res = res[(res.y >= 0)]
        subsets = get_subsets(res['x'].values)

        for first, last in subsets:
            x = res[first:last]['x']
            y = res[first:last]['y']

            plt.ylabel('$x$')
            plt.xlabel('$y$')
            plt.plot(x, y, '-')

    return res['x'], res['y']
