import unittest
from remove_punctuations import remove_punctuations


class TestRemovePunctuations(unittest.TestCase):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    def test_remove_punctuations(self):
        # Test removal of punctuations from a string
        self.assertEqual(remove_punctuations("Hello, world!"), "Hello world")

        # Test removal of punctuations from an empty string
        self.assertEqual(remove_punctuations(""), "")

        # Test removal of punctuations from a string with no punctuations
        self.assertEqual(remove_punctuations(
            "The quick brown fox jumps over the lazy dog"), "The quick brown fox jumps over the lazy dog")

        sef.assertEqual(remove_punctuations("Hello!!!, how are you? -Hope doing well."),
                        "Hello how are you Hope doing well")

        sef.assertEqual(remove_punctuations(
            '''!()-[]{};:'"\,<>./?@#$%^&*_~'''), "")


if __name__ == '__main__':
    unittest.main()
