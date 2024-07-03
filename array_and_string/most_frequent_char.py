from collections import Counter

"""
Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most
frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.
"""


# Using Counters
# def most_frequent_char(s):
#   return Counter(s).most_common(1)[0][0]


# Using hash map
def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    most_freq_char = None
    most_freq_char_count = 0
    for char, char_count in count.items():
        if char_count > most_freq_char_count:
            most_freq_char = char
            most_freq_char_count = char_count

    return most_freq_char


# n = length of string
# Time: O(n)
# Space: O(n)


assert most_frequent_char("bookeeper") == "e"
