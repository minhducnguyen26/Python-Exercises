import unittest

from reverse_words import reverse_words


class TestReverseWords(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(reverse_words("Hello, world!"), "world! Hello,")
        self.assertEqual(reverse_words("Python is fun"), "fun is Python")
        self.assertEqual(reverse_words(
            "A man a plan a canal Panama"), "Panama canal a plan a man A")


if __name__ == '__main__':
    unittest.main()
