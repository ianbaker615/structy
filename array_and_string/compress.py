"""
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'

You can assume that the input only contains alphabetic characters.
"""


def compress(s):
    result = []
    s += "!"  # Prevent out of bounds error when looking forward at last char
    i = 0
    while i < len(s) - 1:
        char = s[i]
        count = 1
        while s[i] == s[i + 1]:
            count += 1
            i += 1

        if count == 1:
            result.append(char)
        else:
            result.append(str(count) + char)
        i += 1

    return "".join(result)


# n = length of string
# Time: O(n)
# Space: O(n)

assert compress('ccaaatsss') == "2c3at3s"
