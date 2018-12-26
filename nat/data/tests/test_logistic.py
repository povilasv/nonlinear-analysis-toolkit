import unittest
import matplotlib.pyplot as plt
from nat.data import logistic_map


class TestLogistic(unittest.TestCase):
    def test_default(self):
        x = logistic_map()
        self.assertEqual(x[0], 0.51)

    def test_length_10(self):
        length = 10
        x = logistic_map(length=length)

        self.assertEqual(len(x), length)

    def test_length_1(self):
        length = 1
        x = logistic_map(length=length)

        self.assertEqual(len(x), length)

    def test_plot(self):
        # plt.clf()
        logistic_map(plot=True)
        # plt.show()


if __name__ == '__main__':
    unittest.main()
