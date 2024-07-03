"""Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple
containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.
"""


def pair_sum(numbers, target_sum):
    complements = {}
    for i, num in enumerate(numbers):
        if num in complements:
            return (complements[num], i)
        complement = target_sum - num
        complements[complement] = i


# n = length of numbers list
# Time: O(n)
# Space: O(n)


assert pair_sum([3, 2, 5, 4, 1], 8) == (0, 2)
