from typing import List


# class Solution:
#     """
#     Given an array of integers nums and an integer target, return indices of
#     the two numbers such that they add up to target.
#     You may assume that each input would have exactly one solution, and you
#     may not use the same element twice. You can return the answer in any order.
#     """
#     def two_sum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(0, len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return i, j
#         return None, None


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        previous = {}

        for a in range(len(nums)):
            y = target - nums[a]
            if y in previous:
                return previous[y], a
            previous[nums[a]] = a
        return None, None
