
from utils import *
from .defaults import default_delay



def lle_kantz(x, min_m=2, max_m=None, d=None, t=0, min_epsilon=None, max_epsilon=None, num_epsilon=5, s=50,
              should_plot=False, plot_title=None):
    """
        Uses tisean library to compute largest lyapunov exponent using Kantz algorithm.

        More info:
        http://www.mpipks-dresden.mpg.de/~tisean/Tisean_3.0.1/docs/docs_c/lyap_k.html
    :param x: time series.
    :param min_m: minimal embedding dimension.
    :param max_m: maximal embedding dimension.
    :param t: theiler window
    :param d: delay to use, if None calculates delay using :func find_autocorr_drop.
    :param s: number of iterations.
    :param should_plot: when True, plots figures.
    :return: largest Lyapunov exponent value.
    """
    if max_m is None or math.isnan(max_m):
        max_m = min_m
    assert min_m <= max_m

    if d is None:
        d = default_delay(x=x, should_plot=should_plot)

    tmp_file = 'tmp/lyap_k_{0}.dat'.format(min_m)
    if os.path.isfile(tmp_file):
        os.remove(tmp_file)

    tisean.lyap_k(input=x, m=min_m, M=max_m, d=d, r=min_epsilon, R=max_epsilon, hashtag=num_epsilon, t=t, s=s,
                  o=tmp_file)

    if os.path.getsize(tmp_file) == 0:
        return float('NaN')

    # 1 Number of the iteration
    # 2. The logarithm of the stretching factor (the slope is the Lyapunov exponent if it is a straight line)
    # 3. The number of points for which a neighborhood with enough points was found
    res = pd.read_csv(tmp_file, header=None, delimiter=' ', skip_blank_lines=True,
                      comment='#',
                      names=['iteration', 'stretch', 'points']);
    if res.empty:
        return float('nan')

    subsets = get_subsets(res['iteration'].values)
    lyaps = np.empty(len(subsets))
    i = 0
    for first, last in subsets:
        x = res[first:last]['iteration'].values
        y = res[first:last]['stretch'].values
        lyaps[i] = find_slope(x, y, epsilon=y.std() / 2, line_above=y.std() / 1.5, should_plot=should_plot,
                              plot_title=plot_title)
        # print lyaps[i]
        i += 1

    series = pd.Series(lyaps)
    # if should_plot:
    #     plt.figure()
    #     # plt.xlabel('m')
    #     plt.ylabel('$\lambda$')
    #     series.plot()
    # print series
    return series.median()
