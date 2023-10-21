"""
Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""


import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        sorted_elements = sorted(count.keys(), key=lambda x: (-count[x], x))
        return sorted_elements[:k]
