import unittest
import matplotlib.pyplot as plt
from nat.data import lorenz_equations


class TestLorenz(unittest.TestCase):
    def test_default(self):
        x, y, z = lorenz_equations()
        self.assertEqual(x[0], 4.752)
        self.assertEqual(y[0], 1.351)
        self.assertEqual(z[0], 27.563000000000002)

    def test_length_10(self):
        length = 10
        x, y, z = lorenz_equations(length=length)

        self.assertEqual(len(x), length)
        self.assertEqual(len(y), length)
        self.assertEqual(len(z), length)

    def test_length_1(self):
        length = 1
        x, y, z = lorenz_equations(length=length)

        self.assertEqual(len(x), length)
        self.assertEqual(len(y), length)
        self.assertEqual(len(z), length)

    def test_plot(self):
        lorenz_equations(plot=True)
        # plt.show()

if __name__ == '__main__':
    unittest.main()
