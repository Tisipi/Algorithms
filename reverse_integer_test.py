import unittest

from reverse_integer import reverse_integer


class TestReverseInteger(unittest.TestCase):
    def test_reverse_integer_zero(self):
        self.assertEqual(reverse_integer(0), 0)

    def test_reverse_integer_1_digit(self):
        self.assertEqual(reverse_integer(5), 5)

    def test_reverse_integer_2_digits(self):
        self.assertEqual(reverse_integer(15), 51)
        self.assertEqual(reverse_integer(92), 29)
        self.assertEqual(reverse_integer(123456789), 987654321)

    def test_reverse_integer_2_digits_with_zero(self):
        self.assertEqual(reverse_integer(10), 1)
        self.assertEqual(reverse_integer(90), 9)
        self.assertEqual(reverse_integer(9000000), 9)

    def test_reverse_negative_integer(self):
        self.assertEqual(reverse_integer(-15), -51)
        #
        self.assertEqual(reverse_integer(-90), -9)
        self.assertEqual(reverse_integer(-9000000), -9)

    def test_reverse_invalid_input_float(self):
        # reverse_integer(3.5)
        self.assertRaises(ValueError, reverse_integer, 3.5)

    def test_reverse_invalid_input_string(self):
        # reverse_integer('Nice')
        self.assertRaises(ValueError, reverse_integer, "Nice")


if __name__ == "__main__":
    unittest.main()
