"""
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:
<number><char>
for example, '2c' or '3a'.
The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
"""


def uncompress(s):
    result = []
    i = 0
    while i < len(s):
        num = ""
        while s[i].isnumeric():
            num += s[i]
            i += 1
        result.append(s[i] * int(num))
        i += 1
    return "".join(result)


# n = number of groups
# m = max num found in any group
# Time: O(n*m)
# Space: O(n*m)

assert uncompress("2c3a1t") == "ccaaat"
