import unittest

from calculate_circle_area import calculate_circle_area


class TestCalculateCircleArea(unittest.TestCase):
    def test_calculate_circle_area(self):
        self.assertAlmostEqual(calculate_circle_area(1),
                               3.14159265359, places=10)
        self.assertAlmostEqual(calculate_circle_area(
            2.5), 19.63495408494, places=10)
        self.assertAlmostEqual(calculate_circle_area(0), 0, places=10)


if __name__ == '__main__':
    unittest.main()
