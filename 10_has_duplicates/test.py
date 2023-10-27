import unittest

from has_duplicates import has_duplicates


class TestHasDuplicates(unittest.TestCase):
    def test_has_duplicates(self):
        self.assertTrue(has_duplicates([1, 2, 3, 4, 3, 5]))
        self.assertFalse(has_duplicates([1, 2, 3, 4, 5, 6]))
        self.assertTrue(has_duplicates(["apple", "banana", "apple", "cherry"]))
        self.assertFalse(has_duplicates([]))


if __name__ == '__main__':
    unittest.main()
