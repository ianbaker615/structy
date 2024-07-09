"""Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list
containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.
"""


def intersection(a, b):
    return list(set(a).intersection(set(b)))


# n = length of array a
# m = length of array b
# Time: O(n + m)
# Space: O(n)

assert intersection([4, 2, 1, 6], [3, 6, 9, 2, 10]) == [2, 6]
