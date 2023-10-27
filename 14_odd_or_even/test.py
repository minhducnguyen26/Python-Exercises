import unittest

from odd_or_even import odd_or_even


class TestOddOrEven(unittest.TestCase):
    def test_odd_or_even(self):
        # Test odd input
        self.assertEqual(odd_or_even(1), "odd")

        # Test even input
        self.assertEqual(odd_or_even(2), "even")

        # Test zero input
        self.assertEqual(odd_or_even(0), "even")

        # Test negative odd input
        self.assertEqual(odd_or_even(-3), "odd")

        # Test negative even input
        self.assertEqual(odd_or_even(-4), "even")


if __name__ == '__main__':
    unittest.main()
