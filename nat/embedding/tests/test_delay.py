import unittest
import numpy as np
from numpy.testing import assert_array_equal
from nat.embedding import delay_vector


class DelayTest(unittest.TestCase):
    def test_delay_vector(self):
        x = [1, 2, 3]
        delays = delay_vector(x)
        assert_array_equal(delays, np.array([[1], [2], [3]]))

    def test_delay_vector_plot(self):
        x = [1, 2, 3]
        delay_vector(x, plot=True)

    def test_delay_vector_d_2_m_2(self):
        x = [1, 2, 3, 4, 5]
        d = 2
        m = 2
        delays = delay_vector(x, d=d, m=m)
        assert_array_equal(delays, np.array([[3, 1], [4, 2], [5, 3]]))
