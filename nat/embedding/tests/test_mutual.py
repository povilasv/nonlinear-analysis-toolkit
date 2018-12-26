import unittest
from nat.embedding import mutual_information, delay_mutual, find_mutual_min
from nat.data import logistic_map
import numpy as np


class TestMutualInformation(unittest.TestCase):
    def test_mutual_information(self):
        x = logistic_map(length=200)

        x, y = mutual_information(x=x)
        self.assertEqual(x[0], 0)
        self.assertEqual(x[1], 1)
        self.assertEqual(y[0], np.float32(2.502028))

    def test_mutual_information_100(self):
        D = 100
        x = logistic_map(length=100)

        x, y = mutual_information(x=x, max_d=D)
        self.assertEqual(len(x), 100)
        self.assertEqual(len(y), 100)

    def test_mutual_information_plot(self):
        x = logistic_map(length=500)

        mutual_information(x=x, plot=True)


class TestFindMutualMin(unittest.TestCase):
    def test_find_mutual_min(self):
        x = logistic_map(length=200)

        d = find_mutual_min(x=x)
        self.assertEqual(d, 7)

    def test_find_mutual_min_100(self):
        D = 100
        x = logistic_map(length=200)

        d = find_mutual_min(x=x, max_d=D)
        self.assertEqual(d, 7)


class TestDelayMutual(unittest.TestCase):
    def test_delay_mutual(self):
        x = xrange(0, 500)
        d = delay_mutual(x=x)
        self.assertEqual(d, 17)
