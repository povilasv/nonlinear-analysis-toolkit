"""
The :mod:`nat.data` module includes time series generation methods.
"""

from .henon import henon_map
from .ikeda import ikeda_map
from .logistic import logistic_map
from .lorenz import lorenz_equations
from .lozi import lozi_map
from .rossler import rossler_system
from .tent import tent_map

from . import henon
from . import ikeda
from . import logistic
from . import lorenz
from . import lozi
from . import rossler
from . import tent

__all__ = ["henon_map", "ikeda_map", "logistic_map",
           "lorenz_equations", "lozi_map", "rossler_system",
           "henon", "ikeda", "logistic", "lorenz_equations",
           "lozi_map", "rossler_system", "tent_map"]
