import unittest

from sort_words import *


class TestSortWords(unittest.TestCase):
    def test_sort_words_alphabetically_in_list(self):
        # Test sorting of words in a list
        self.assertEqual(sort_words_alphabetically_in_list(
            ["Hello", "World", "Apple", "Banana"]), ["Apple", "Banana", "Hello", "World"])

        # Test sorting of words in an empty list
        self.assertEqual(sort_words_alphabetically_in_list([]), [])

        # Test sorting of words in a list with one word
        self.assertEqual(
            sort_words_alphabetically_in_list(["Hello"]), ["Hello"])

    def test_sort_words_alphabetically_in_string(self):
        # Test sorting of words in a string
        self.assertEqual(sort_words_alphabetically_in_string(
            "Hello World Apple Banana"), "Apple Banana Hello World")

        # Test sorting of words in an empty string
        self.assertEqual(sort_words_alphabetically_in_string(""), "")

        # Test sorting of words in a string with one word
        self.assertEqual(sort_words_alphabetically_in_string("Hello"), "Hello")

    def test_sort_words_by_length_in_list(self):
        # Test sorting of words in a list by length
        self.assertEqual(sort_words_by_length_in_list(
            ["Hello", "World", "Apple", "Banana"]), ["Apple", "Banana", "World", "Hello"])

        # Test sorting of words in an empty list
        self.assertEqual(sort_words_by_length_in_list([]), [])

        # Test sorting of words in a list with one word
        self.assertEqual(sort_words_by_length_in_list(["Hello"]), ["Hello"])

    def test_sort_words_by_length_in_string(self):
        # Test sorting of words in a string by length
        self.assertEqual(sort_words_by_length_in_string(
            "Hello World Apple Banana"), "Apple Banana Hello World")

        # Test sorting of words in an empty string
        self.assertEqual(sort_words_by_length_in_string(""), "")

        # Test sorting of words in a string with one word
        self.assertEqual(sort_words_by_length_in_string("Hello"), "Hello")


if __name__ == '__main__':
    unittest.main()
