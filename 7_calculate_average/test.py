import unittest

from calculate_average import calculate_average


class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average(self):
        self.assertAlmostEqual(calculate_average(
            [1, 2, 3, 4, 5]), 3.0, places=2)
        self.assertAlmostEqual(calculate_average(
            [10, 20, 30, 40, 50]), 30.0, places=2)
        self.assertAlmostEqual(calculate_average([]), 0, places=2)


if __name__ == '__main__':
    unittest.main()
