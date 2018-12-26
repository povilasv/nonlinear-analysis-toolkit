import unittest
from nat.data import tent_map


class TestTent(unittest.TestCase):
    def test_default(self):
        x = tent_map()
        self.assertEqual(x[0], 0.51)

    def test_length_10(self):
        length = 10
        x = tent_map(length=length)

        self.assertEqual(len(x), length)

    def test_length_1(self):
        length = 1
        x = tent_map(length=length)

        self.assertEqual(len(x), length)

    def test_plot(self):
        tent_map(plot=True, length=500)


if __name__ == '__main__':
    unittest.main()
