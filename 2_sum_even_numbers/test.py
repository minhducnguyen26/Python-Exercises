import unittest

from sum_even_numbers import sum_even_numbers


class TestSumEvenNumbers(unittest.TestCase):
    def test_sum_even_numbers(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5, 6]), 12)
        self.assertEqual(sum_even_numbers([2, 4, 6, 8, 10]), 30)
        self.assertEqual(sum_even_numbers([1, 3, 5, 7, 9]), 0)


if __name__ == '__main__':
    unittest.main()
