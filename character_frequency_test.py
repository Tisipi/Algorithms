import unittest
from character_frequency import Character_Frequency


EMPTY_STRING = ""
STRING_WITH_ONE_SPACE = " "
STRING_WITH_ONE_CHAR = "a"
STRING_WITH_ONE_SPECIAL_CHAR = "$"

STRING_MAX_a_COUNT_1 = "abcdef123456"
STRING_MAX_f_COUNT_2 = "abcdef123456f"
STRING_MAX_1_COUNT_3 = "abcdef123456f121"
STRING_MAX_X_COUNT_4 = "X 123456X7890 abcXdefgh X"


class Test_Character_Frequency(unittest.TestCase):
    def test_max_char_empty_string(self):
        char_freq = Character_Frequency(EMPTY_STRING)
        self.assertEqual(char_freq.most_occurring_char(), None)
        self.assertEqual(char_freq.highest_frequency(), 0)

    def test_max_char_in_string_with_one_char(self):
        char_freq = Character_Frequency(STRING_WITH_ONE_SPACE)
        self.assertEqual(char_freq.most_occurring_char(), " ")
        self.assertEqual(char_freq.highest_frequency(), 1)

        char_freq = Character_Frequency(STRING_WITH_ONE_CHAR)
        self.assertEqual(char_freq.most_occurring_char(), "a")
        self.assertEqual(char_freq.highest_frequency(), 1)

        char_freq = Character_Frequency(STRING_WITH_ONE_SPECIAL_CHAR)
        self.assertEqual(char_freq.most_occurring_char(), "$")
        self.assertEqual(char_freq.highest_frequency(), 1)

    def test_max_char(self):
        char_freq = Character_Frequency(STRING_MAX_a_COUNT_1)
        self.assertEqual(char_freq.most_occurring_char(), "a")
        self.assertEqual(char_freq.highest_frequency(), 1)

        char_freq = Character_Frequency(STRING_MAX_f_COUNT_2)
        self.assertEqual(char_freq.most_occurring_char(), "f")
        self.assertEqual(char_freq.highest_frequency(), 2)

        char_freq = Character_Frequency(STRING_MAX_1_COUNT_3)
        self.assertEqual(char_freq.most_occurring_char(), "1")
        self.assertEqual(char_freq.highest_frequency(), 3)

        char_freq = Character_Frequency(STRING_MAX_X_COUNT_4)
        self.assertEqual(char_freq.most_occurring_char(), "X")
        self.assertEqual(char_freq.highest_frequency(), 4)

    def test_frequency_of_char(self):
        char_freq = Character_Frequency(STRING_MAX_X_COUNT_4)
        self.assertEqual(char_freq.frequency_of_char("z"), 0)
        self.assertEqual(char_freq.frequency_of_char("a"), 1)
        self.assertEqual(char_freq.frequency_of_char("X"), 4)


if __name__ == "__main__":
    unittest.main()
