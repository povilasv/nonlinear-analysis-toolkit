import unittest
import numpy as np
from nat.utilities import add_noise


class TestNoise(unittest.TestCase):
    def test_add_uniform_noise(self):
        x = np.array([0, 1, 0, 1])
        y = add_noise(x, percentage=100, type='uniform')
        self.assertEqual(len(y), len(x))

    def test_add_gaussian_noise(self):
        x = np.array([0, 1, 0, 1])
        y = add_noise(x, percentage=100, type='gaussian')
        self.assertEqual(len(y), len(x))

    def test_plot(self):
        x = np.array([0, 1, 0, 1])
        add_noise(x, percentage=100, plot=True)
