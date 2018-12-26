import unittest
import matplotlib.pyplot as plt
from nat.data import henon_map


class TestHenon(unittest.TestCase):
    def test_default(self):
        x, y = henon_map()
        self.assertEqual(x[0], 0.51)
        self.assertEqual(y[0], 0.51)

    def test_length_10(self):
        length = 10
        x, y = henon_map(length=length)

        self.assertEqual(len(x), length)
        self.assertEqual(len(y), length)

    def test_length_1(self):
        length = 1
        x, y = henon_map(length=length)

        self.assertEqual(len(x), length)
        self.assertEqual(len(y), length)

    def test_plot(self):
        henon_map(plot=True)
        # plt.show()

if __name__ == '__main__':
    unittest.main()
