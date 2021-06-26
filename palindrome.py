from reverse_string import reverse_string_simple


def is_palindrome(my_string):
    PUNCTUATIONS = '''!()-;:'",./?&'''
    new_string = my_string.lower().replace(' ', '')
    new_string = ''.join(char for char in new_string if char not in PUNCTUATIONS)
    return (new_string == reverse_string_simple(new_string))
