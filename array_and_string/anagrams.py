from collections import Counter

"""Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean 
indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, 
but in any order."""


# Count solution
# def anagrams(s1, s2):
#   return Counter(s1) == Counter(s2)


# Hash map solution
def anagrams(s1, s2):
    count_1 = build_count_dict(s1)
    count_2 = build_count_dict(s2)
    return count_1 == count_2


def build_count_dict(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    return count


# n = length of string 1
# m = length of string 2
# Time: O(n + m)
# Space: O(n + m)

assert anagrams('restful', 'fluster') is True
