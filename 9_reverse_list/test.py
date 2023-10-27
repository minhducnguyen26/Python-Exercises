import unittest

from reverse_list import reverse_list


class TestReverseList(unittest.TestCase):
    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_list(["apple", "banana", "cherry"]), [
                         "cherry", "banana", "apple"])
        self.assertEqual(reverse_list([]), [])


if __name__ == '__main__':
    unittest.main()
