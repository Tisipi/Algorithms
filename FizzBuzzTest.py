import unittest
from FizzBuzz import fizz_buzz

#  print "Fizz" instead of the number
# - for multiples of five print "Buzz"
# - for multiples of both three and five print "FizzBuzz"


class Test_FizzBuzz(unittest.TestCase):
    def test_fizz(self):
        multiples_of_three = [3, 6, 9, 12, 18, 21, 24, 27, 33]
        for number in multiples_of_three:
            self.assertEqual(fizz_buzz(number), "Fizz")

    def test_buzz(self):
        multiples_of_five = [5, 10, 20, 25, 35]
        for number in multiples_of_five:
            self.assertEqual(fizz_buzz(number), "Buzz")

    def test_fizz_buzz(self):
        multiples_of_fifteen = [15, 30, 45, 60, 75]
        for number in multiples_of_fifteen:
            self.assertEqual(fizz_buzz(number), "FizzBuzz")

    def test_numbers_without_fizz_buzz(self):
        numbers = [
            1,
            2,
            4,
            7,
            8,
            11,
            13,
            14,
            16,
            17,
            19,
        ]
        for number in numbers:
            self.assertEqual(fizz_buzz(number), number)

    def test_number_zero(self):
        self.assertRaises(ValueError, fizz_buzz, 0)

    def test_number_negative(self):
        self.assertRaises(ValueError, fizz_buzz, -10)

    def test_not_an_integer(self):
        self.assertRaises(ValueError, fizz_buzz, 1.6)
        self.assertRaises(ValueError, fizz_buzz, "haha")


if __name__ == "__main__":
    unittest.main()
