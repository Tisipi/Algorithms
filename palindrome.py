from reverse_string import reverse_string


def is_palindrome(my_string):
    PUNCTUATIONS = """!()-;:'",./?&"""
    new_string = my_string.lower().replace(" ", "")
    new_string = "".join(char for char in new_string if char not in PUNCTUATIONS)
    return new_string == reverse_string(new_string)
