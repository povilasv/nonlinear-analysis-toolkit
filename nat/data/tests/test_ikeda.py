import unittest
import matplotlib.pyplot as plt
from nat.data import ikeda_map


class TestIkeda(unittest.TestCase):
    def test_default(self):
        x, y = ikeda_map()
        self.assertEqual(x[0], 1.43300927)
        self.assertEqual(y[0], 0.39006453799999996)

    def test_length_10(self):
        length = 10
        x, y = ikeda_map(length=length)

        self.assertEqual(len(x), length)
        self.assertEqual(len(y), length)

    def test_length_1(self):
        length = 1
        x, y = ikeda_map(length=length)

        self.assertEqual(len(x), length)
        self.assertEqual(len(y), length)

    def test_plot(self):
        ikeda_map(plot=True)
        plt.show()

if __name__ == '__main__':
    unittest.main()
