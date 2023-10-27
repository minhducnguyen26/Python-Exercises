import unittest

from count_words import count_words


class TestCountWords(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("Hello, world!"), 2)
        self.assertEqual(count_words("Python is fun"), 3)
        self.assertEqual(count_words(""), 0)


if __name__ == '__main__':
    unittest.main()
