import unittest
from reverse_string import (
    reverse_string,
    reverse_string_iterative,
    reverse_string_recursive,
)

EMPTY_STRING = ""
ONE_CHAR_STRING = "a"
STRING = "abc9def"
REVERSED_STRING = "fed9cba"


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string(EMPTY_STRING), EMPTY_STRING)
        self.assertEqual(reverse_string(ONE_CHAR_STRING), ONE_CHAR_STRING)
        self.assertEqual(reverse_string(STRING), REVERSED_STRING)

    def test_reverse_string_iterative(self):
        self.assertEqual(reverse_string_iterative(EMPTY_STRING), EMPTY_STRING)
        self.assertEqual(reverse_string_iterative(ONE_CHAR_STRING), ONE_CHAR_STRING)
        self.assertEqual(reverse_string_iterative(STRING), REVERSED_STRING)

    def test_reverse_string_recursive(self):
        self.assertEqual(reverse_string_recursive(EMPTY_STRING), EMPTY_STRING)
        self.assertEqual(reverse_string_recursive(ONE_CHAR_STRING), ONE_CHAR_STRING)
        self.assertEqual(reverse_string_recursive(STRING), REVERSED_STRING)


if __name__ == "__main__":
    unittest.main()
