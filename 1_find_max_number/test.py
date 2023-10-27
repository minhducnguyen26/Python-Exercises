import unittest

from find_max_number import find_max_number


class TestFindMaxNumber(unittest.TestCase):
    def test_find_max_number(self):
        self.assertEqual(find_max_number([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max_number([-1, 0, 5, 2, -3]), 5)
        self.assertEqual(find_max_number([]), None)


if __name__ == '__main__':
    unittest.main()
