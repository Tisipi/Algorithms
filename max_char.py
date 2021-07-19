def max_char(str):
    # Returns most occurring character (and its frequency) in string.
    max = 0
    max_elem = None
    character_frequency = frequency_of_chars_in_string(str)
    for elem in character_frequency:
        if character_frequency[elem] > max:
            max = character_frequency[elem]
            max_elem = elem
    return (max_elem, max)


def frequency_of_chars_in_string(str):
    # Calculate number of occurrences of each character in string.
    # Returns character frequency dictionary.
    character_frequency = {}
    for char in str:
        if not char in character_frequency:
            character_frequency[char] = 0
        character_frequency[char] += 1
    return character_frequency
