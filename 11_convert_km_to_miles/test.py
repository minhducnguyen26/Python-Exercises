import unittest

from convert_km_to_miles import convert_km_to_miles


class TestConvertKmToMiles(unittest.TestCase):
    def test_convert_km_to_miles(self):
        self.assertAlmostEqual(convert_km_to_miles(1), 0.621371, places=6)
        self.assertAlmostEqual(convert_km_to_miles(10), 6.21371, places=5)
        self.assertAlmostEqual(convert_km_to_miles(100), 62.1371, places=4)


if __name__ == '__main__':
    unittest.main()
