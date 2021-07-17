def reverse_integer(number):

    # Does not cover overflow errors

    if not isinstance(number, int):
        raise ValueError("Not an integer")

    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    reversed_integer = 0
    while number != 0:
        remainder = number % 10
        reversed_integer = reversed_integer * 10 + remainder
        number = number // 10
    if is_negative:
        return -reversed_integer
    else:
        return reversed_integer
