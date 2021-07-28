def fizz_buzz(number):
    """
    fizz_buzz returns a given number if it is not a multiple of three or five, but:
    - for multiples of three it returns "Fizz"
    - for multiples of five it returns "Buzz"
    - for multiples of both three and five it returns "FizzBuzz"
    """
    if not isinstance(number, int):
        raise ValueError("Not an integer")
    if number <= 0:
        raise ValueError("Number must be greater than zero")
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number


if __name__ == "__main__":
    for i in range(1, 46):
        print(i, fizz_buzz(i))
