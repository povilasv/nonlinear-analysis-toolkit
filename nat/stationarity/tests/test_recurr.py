import unittest
from nat.stationarity import recurrence_plot
from nat.data import logistic_map
import matplotlib.pyplot as plt

class TestRecurrence(unittest.TestCase):
    def test_recurr(self):
        x = logistic_map(length=200)
        x, y, = recurrence_plot(x=x, m=1)
        self.assertEqual(x[0], 1)
        self.assertEqual(y[0], 182)
    # TODO: what is this?
    def test_recurr_plot(self):
        x = logistic_map(length=200)
        data = recurrence_plot(x=x, m=1, plot=True)
        plt.show()
