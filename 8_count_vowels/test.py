import unittest

from count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("python"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("rhythm"), 0)


if __name__ == '__main__':
    unittest.main()
