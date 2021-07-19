import unittest
from max_char import max_char

EMPTY_STRING = ""
STRING_WITH_ONE_SPACE = " "
STRING_WITH_ONE_CHAR = "a"
STRING_WITH_ONE_SPECIAL_CHAR = "$"

STRING_MAX_a_COUNT_1 = "abcdef123456"
STRING_MAX_f_COUNT_2 = "abcdef123456f"
STRING_MAX_1_COUNT_3 = "abcdef123456f121"
STRING_MAX_X_COUNT_4 = "X 123456X7890 abcXdefgh X"


class TestMaxChar(unittest.TestCase):
    def test_max_char_empty_string(self):
        self.assertEqual(max_char(EMPTY_STRING), (None, 0))

    def test_max_char_in_string_with_one_char(self):
        self.assertEqual(max_char(STRING_WITH_ONE_SPACE), (" ", 1))
        self.assertEqual(max_char(STRING_WITH_ONE_CHAR), ("a", 1))
        self.assertEqual(max_char(STRING_WITH_ONE_SPECIAL_CHAR), ("$", 1))

    def test_max_char(self):
        self.assertEqual(max_char(STRING_MAX_a_COUNT_1), ("a", 1))
        self.assertEqual(max_char(STRING_MAX_f_COUNT_2), ("f", 2))
        self.assertEqual(max_char(STRING_MAX_1_COUNT_3), ("1", 3))
        self.assertEqual(max_char(STRING_MAX_X_COUNT_4), ("X", 4))


if __name__ == "__main__":
    unittest.main()
