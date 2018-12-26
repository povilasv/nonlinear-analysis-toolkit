import unittest
from nat.embedding import embeded_dim_kennel
from nat.data import logistic_map
import numpy as np
import matplotlib.pyplot as plt


class TestEmbeddedDimKennel(unittest.TestCase):
    def test_embeded_dim_kennel(self):
        x = logistic_map(length=200)

        dim = embeded_dim_kennel(x=x)
        self.assertEqual(dim, 2)

    def test_embeded_dim_kennel_plot(self):
        x = logistic_map(length=200)

        dim = embeded_dim_kennel(x=x, plot=True)
        self.assertEqual(dim, 2)

    def test_embeded_dim_kennel_long(self):
        x = logistic_map(length=1500)
        # Theoretical correlation dimension value is between 0.4926 and 0.5024.
        # https://en.wikipedia.org/wiki/Logistic_map
        dim = embeded_dim_kennel(x, d=1, min_m=1, max_m=10)
        self.assertEqual(dim, 1)
