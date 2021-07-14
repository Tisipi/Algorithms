def reverse_string(my_string):
    return my_string[::-1]


def reverse_string_iterative(my_string):
    reversed_string = ""
    for char in my_string:
        reversed_string = char + reversed_string
    return reversed_string


def reverse_string_recursive(my_string):
    if my_string == "":
        return ""
    else:
        return reverse_string_recursive(my_string[1:]) + my_string[0]
