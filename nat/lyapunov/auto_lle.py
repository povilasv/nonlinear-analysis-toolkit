from dependencies import *
from chaos_utils import embeded_dim_kennel, space_time_plot, lle_kantz, lle_rosenstein, \
    lle_rosenstein_range, delay_mutual, delay_autocorr
from utils import simple_moving_average

delay_methods = ['mutual_information', 'filtered_mutual_information', 'autocorrelation']
lle_methods = ['Kantz', 'Rosenstein', 'Rosenstein_range']


# TODO: params
def estimate_auto_lle(x, max_m=20, w=10, s=50, delay_method='filtered_mutual_information',
                      lle_method='Rosenstein', num_time_step=60, fraction=0.1, debug=False, should_plot=False,
                      should_plot2=False):
    """
        Automatic correlation dimension computation using system described in
        TODO: link to my algorithm.
    :param x:
    :param max_m:
    :param w:
    :param epsilon:
    :param num_time_step:
    :param fraction:
    :param should_plot:
    :return:
    """

    if delay_method not in delay_methods:
        raise ValueError('Error: delay method {0} not found. '
                         'Try from {1}'.format(delay_method, delay_methods))

    if lle_method not in lle_methods:
        raise ValueError('Error: LLE method {0} not found. '
                         'Try from {1}'.format(lle_method, lle_methods))

    if delay_method == 'mutual_information':
        d = delay_mutual(x, should_plot=should_plot)
    elif delay_method == 'filtered_mutual_information':
        d = delay_mutual(simple_moving_average(x, window=w), should_plot=should_plot)
    elif delay_method == 'autocorrelation':
        d = delay_autocorr(x, should_plot=should_plot)

    if d is None:
        print 'Error: cannot estimate delay'
        return None

    if debug:
        print 'Reconstruction delay L={0}'.format(d)
    if should_plot:
        plt.figure()

    embedded_dim = embeded_dim_kennel(x, d=d, max_m=max_m, should_plot=should_plot)
    if embedded_dim is None or math.isnan(embedded_dim):
        print 'Error: could not estimate embedded_dim'
        return None

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

    if lle_method == 'Kantz':
        lle = lle_kantz(x, max_m=max_m, d=d, s=s, t=theiler_window, should_plot=should_plot2)
    elif lle_method == 'Rosenstein':
        lle = lle_rosenstein(x, m=embedded_dim, d=d, s=s, t=theiler_window, should_plot=should_plot2)
    elif lle_method == 'Rosenstein_range':
        lle = lle_rosenstein_range(x, max_m=max_m, d=d, s=s, t=theiler_window, should_plot=should_plot)

    return lle
