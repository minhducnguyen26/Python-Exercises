import unittest
from random_number import random_number


class TestRandomNumber(unittest.TestCase):
    def test_random_number(self):
        # Test that the random number is between 1 and 100
        for i in range(100):
            self.assertGreaterEqual(random_number(), 1)
            self.assertLessEqual(random_number(), 100)


if __name__ == '__main__':
    unittest.main()
