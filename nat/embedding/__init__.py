# Another possible option to use autocorrelation
# DELAY_ESTIMATION_METHOD = 'autocorrelation'
DELAY_ESTIMATION_METHOD = 'mutual_information'
DELAY_SEARCH_LIMIT = 1000000
DELAY_SEARCH_START = 1000

def default_delay(x, plot=False):
    """
        This functions set's default delay estimation method.

    :param x: time series.
    :param plot: Should plot be produced?
    :return: reconstruction delay value.
    """

    if DELAY_ESTIMATION_METHOD == 'mutual_information':
        return delay_mutual(x=x, plot=plot)

    if DELAY_ESTIMATION_METHOD == 'autocorrelation':
        return delay_autocorr(x=x, plot=plot)


from .mutual import delay_mutual, mutual_information, find_mutual_min
from .delay import delay_vector
from .false_nearest import embeded_dim_kennel

from . import mutual
from . import delay
from . import false_nearest

__all__ = ["corr", "default_delay", "delay_mutual", "find_mutual_min",
           "mutual_information", "delay_vector", "embeded_dim_kennel"]


