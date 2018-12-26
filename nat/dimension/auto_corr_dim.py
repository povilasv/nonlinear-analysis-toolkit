import matplotlib.pyplot as plt
import math
from chaos_utils import default_delay, embeded_dim_kennel, space_time_plot, corr_dim_fast, delay_mutual, delay_autocorr
from utils import simple_moving_average


# TODO: param
def estimate_auto_corr_dim(x, max_m=20, w=10, epsilon=0.05, delay_method='autocorrelation', num_time_step=60,
                           fraction=0.1, debug=False, should_plot=False):
    """
        Automatic correlation dimension computation using system described in
        TODO: link to my algorithm.
    :param delay_method: mutual_information, filtered_mutual_information or autocorrelation method.
    :param x: time series.
    :param max_m:
    :param w:
    :param epsilon:
    :param num_time_step:
    :param fraction:
    :param should_plot:
    :return:
    """
    if delay_method == 'mutual_information':
        d = delay_mutual(x, should_plot=should_plot)
    elif delay_method == 'filtered_mutual_information':
        d = delay_mutual(simple_moving_average(x, window=w), should_plot=should_plot)
    elif delay_method == 'autocorrelation':
        d = delay_autocorr(x, should_plot=should_plot)

    if d is None:
        print 'Error: cannot estimate delay'
        return None, None

    if debug:
        print 'Reconstruction delay L={0}'.format(d)
    if should_plot:
        plt.figure()

    embedded_dim = embeded_dim_kennel(x, d=d, max_m=max_m, should_plot=should_plot)

    if embedded_dim is None or math.isnan(embedded_dim):
        print 'Error: could not estimate embedded_dim'
        return None, None

    if debug:
        print 'Embedding dimension m={0}'.format(embedded_dim)
    if should_plot:
        plt.figure()

    theiler_window = space_time_plot(x, m=embedded_dim, num_time_step=num_time_step, fraction=fraction,
                                     d=d, should_plot=should_plot)

    if theiler_window is None or math.isnan(theiler_window):
        print 'Warning: could not estimate theiler windows'
        theiler_window = 0

    if debug:
        print 'Theiler window W={0}'.format(theiler_window)

    if should_plot:
        plt.figure()
    corr_dim = corr_dim_fast(x, d=d, min_m=1, max_m=max_m, t=theiler_window,
                             epsilon=epsilon,
                             should_plot=should_plot)

    return corr_dim
