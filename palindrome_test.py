import unittest
from palindrome import is_palindrome


EMPTY_STRING = ''
ONE_CHAR_STRING = 'a'
NOT_A_PALINDROME = 'abc9def'
A_PALINDROME ='madam'
A_PALINDROME_WITH_SPACES = 'never odd or even'
A_PALINDROME_WITH_SPACES_AND_UPPERCASE = 'Never odd or even'
A_PALINDROME_WITH_SPACES_UPPERCASE_AND_PUNCTUATION_1 = 'Mr. Owl ate my metal worm'
A_PALINDROME_WITH_SPACES_UPPERCASE_AND_PUNCTUATION_2 = 'Was it a car or a cat I saw?' 


class TestPalindrome(unittest.TestCase):

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome(EMPTY_STRING))
        self.assertTrue(is_palindrome(ONE_CHAR_STRING))
        self.assertTrue(is_palindrome(A_PALINDROME))

    def test_not_a_palindrome(self):
        self.assertFalse(is_palindrome(NOT_A_PALINDROME))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome(A_PALINDROME_WITH_SPACES))

    def test_palindrome_with_spaces_and_uppercase(self):
        self.assertTrue(is_palindrome(A_PALINDROME_WITH_SPACES_AND_UPPERCASE))

    def test_palindrome_with_spaces_uppercase_and_punctuation(self):
        self.assertTrue(is_palindrome(A_PALINDROME_WITH_SPACES_UPPERCASE_AND_PUNCTUATION_1))
        self.assertTrue(is_palindrome(A_PALINDROME_WITH_SPACES_UPPERCASE_AND_PUNCTUATION_2))


if __name__ == "__main__":
    unittest.main()
