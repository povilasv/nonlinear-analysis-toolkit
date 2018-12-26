
from utils import *
from .defaults import default_delay



def lle_rosenstein(x, m=2, d=None, s=100, t=0, should_plot=False, plot_title=None):
    """
        Uses tisean library to compute largest lyapunov exponent using Rosenstein et al. algorithm.

        More info:
        http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/docs/docs_c/lyap_r.html
    :param t: window around the reference point which should be omitted.
    :param x: time series.
    :param m: embedding dimension to use.
    :param d: delay to use, if None calculates delay using :func find_autocorr_drop.
    :param s: number of iterations.
    :param should_plot:  when True, plots figures.
    :return: largest Lyapunov exponent value.
    """
    if d is None:
        d = default_delay(x=x, should_plot=should_plot)

    tmp_file = 'tmp/lyap_r_{0}_{1}.dat'.format(m, d)
    if os.path.isfile(tmp_file):
        os.remove(tmp_file)

    tisean.lyap_r(input=x, m=m, s=s, d=d, t=t, o=tmp_file)

    if os.path.getsize(tmp_file) == 0:
        return float('NaN')

    # First column: Number of the iteration
    # Second column: Logarithm of the stretching factor
    res = pd.read_csv(tmp_file, sep=' ', comment='#', names=['iteration', 'stretch']);

    x = res.ix[:, 0].values
    y = res.ix[:, 1].values

    lyap = find_slope(x, y, epsilon=y.std() / 2, line_above=y.std()/2, should_plot=should_plot,
                      plot_title=plot_title)

    return lyap


def lle_rosenstein_range(x, min_m=2, max_m=None, d=None, s=50, t=0, should_plot=False,
                         plot_title=None):
    if max_m is None or math.isnan(max_m):
        max_m = min_m

    lyaps = np.empty(max_m - min_m)
    i = 0
    for m in xrange(min_m, max_m):
        lyaps[i] = lle_rosenstein(x=x, m=m, d=d, s=s, t=t, should_plot=should_plot,
                                  plot_title=plot_title)
        i += 1
    # print lyaps
    series = pd.Series(lyaps, index=xrange(min_m, max_m))
    if should_plot:
        plt.figure()
        plt.xlabel('m')
        plt.ylabel('$\lambda$')
        series.plot()

    return np.median(series)
