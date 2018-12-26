import unittest
import matplotlib.pyplot as plt
from nat.data import rossler_system


class TestRossler(unittest.TestCase):
    def test_default(self):
        x, y, z = rossler_system()
        self.assertEqual(x[0], 0)
        self.assertEqual(y[0], 0)
        self.assertEqual(z[0], 0)

    def test_length_10(self):
        length = 10
        x, y, z = rossler_system(length=length)

        self.assertEqual(len(x), length)
        self.assertEqual(len(y), length)
        self.assertEqual(len(z), length)

    def test_length_1(self):
        length = 1
        x, y, z = rossler_system(length=length)

        self.assertEqual(len(x), length)
        self.assertEqual(len(y), length)
        self.assertEqual(len(z), length)

    def test_plot(self):
        # plt.clf()
        rossler_system(plot=True)
        # plt.show()


if __name__ == '__main__':
    unittest.main()
