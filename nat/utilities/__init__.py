"""
The :mod:`nat.utilities` module includes utilities methods.
"""
from .noise import add_noise
from .low_pass_filter import low_pass_filter
from .general import get_subsets, find_first_local_maxima, get_subsets_by_count, get_percentage_diff, find_slope

from . import noise
from . import low_pass_filter
from . import general

__all__ = ["add_noise", "low_pass_filter", "get_subsets", "find_first_local_maxima", "get_subsets_by_count",
           "get_percentage_diff", "find_slope"]
