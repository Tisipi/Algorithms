class Character_Frequency:
    """
    Creates frequency of characters of a given string
    """

    def __init__(self, string):
        self._string = string
        self._frequency = _frequency_of_chars_in_string(string)

    def most_occurring_char(self):
        """Returns most occurring character"""
        max = 0
        max_elem = None
        for elem in self._frequency:
            if self._frequency[elem] > max:
                max = self._frequency[elem]
                max_elem = elem
        return max_elem

    def highest_frequency(self):
        """Returns frequency of most occurring character"""
        max = 0
        for elem in self._frequency:
            if self._frequency[elem] > max:
                max = self._frequency[elem]
        return max

    def frequency_of_char(self, char):
        """Returns frequency of given character"""
        if char in self._frequency:
            return self._frequency[char]
        else:
            return 0


def _frequency_of_chars_in_string(str):
    # Calculate number of occurrences of each character in string.
    # Returns character frequency dictionary.
    character_frequency = {}
    for char in str:
        if not char in character_frequency:
            character_frequency[char] = 0
        character_frequency[char] += 1
    return character_frequency
